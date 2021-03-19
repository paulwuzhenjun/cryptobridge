import hmac
import base64
import hashlib
import logging
import tornado.ioloop
import tornado.web

from bridge_broker.ce_bridge import CEBridge
from bridge_broker.te_bridge import TEBridge


class BridgeBroker:
    mongo_uri: str

    def __init__(self, mongo_uri, port):
        self.mongo_uri = mongo_uri

        self.te_channels = {}
        self.ce_channels = {}

        self.app = tornado.web.Application([
            (r'/bridge/te', TEBridge, {'broker': self}),
            (r'/bridge/ce', CEBridge, {'broker': self}),
        ], websocket_ping_interval=30)
        self.app.listen(port)

        self.logger = logging.getLogger('bridge-broker')

    def run(self):
        self.logger.info(f'run')
        tornado.ioloop.IOLoop.current().start()

    async def on_te_onboard(self, te_id, te_channel):
        self.logger.info(f'te-id: {te_id}, channel: {te_channel}')
        self.te_channels[te_id] = te_channel

    async def on_ce_auth(self, te_id, auth_code, ce_channel):
        self.logger.info(f'te-id: {te_id}, auth-code: {auth_code}, channel: {ce_channel}')
        secret_key = self.mongo_uri.encode()
        digest = hmac.new(secret_key, te_id.encode(), digestmod=hashlib.sha256).digest()
        auth_code_calc = base64.b64encode(digest).decode()
        if auth_code_calc != auth_code:
            return False
        self.ce_channels[te_id] = ce_channel
        return True
