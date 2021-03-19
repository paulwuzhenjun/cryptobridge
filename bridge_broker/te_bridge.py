import json
from typing import Any
import tornado.websocket


class TEBridge(tornado.websocket.WebSocketHandler):
    te_id: [str]
    broker: Any

    def initialize(self, broker):
        self.te_id = None
        self.broker = broker

    async def on_message(self, message):
        message_json = json.loads(message)
        method, path, params = message_json['method'], message_json['path'], message_json['params']
        if method == 'POST':
            await self.on_post(path, params)

    async def on_post(self, path, params):
        if path == '/te/onboard':
            # 策略层登记
            self.te_id = params[0]
            await self.broker.on_te_onboard(self.te_id, self)
