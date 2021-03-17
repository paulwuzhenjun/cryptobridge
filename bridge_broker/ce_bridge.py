import json
import tornado.websocket


class CEBridge(tornado.websocket.WebSocketHandler):
    async def on_message(self, message):
        message_json = json.loads(message)
