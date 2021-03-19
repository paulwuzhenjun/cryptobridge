import json
import logging
from typing import Any, Optional
import tornado.websocket


class CEBridge(tornado.websocket.WebSocketHandler):
    te_id: Optional[str]
    broker: Any

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger('ce-bridge')

    def initialize(self, broker):
        self.te_id = None
        self.broker = broker

    async def on_message(self, message):
        message_json = json.loads(message)
        method, path, params = message_json['method'], message_json['path'], message_json.get('params', [])
        if method == 'POST':
            await self.on_post(path, params)

    async def on_post(self, path, params):
        if path == '/ce/auth':
            # 策略层认证
            te_id, auth_code = params[0], params[1]
            auth_result = await self.broker.on_ce_auth(te_id, auth_code, self)
            if not auth_result:
                self.logger.critical(f'te-id({self.te_id}), auth-code({auth_code}), auth failed')
                self.close()
            else:
                self.te_id = te_id
