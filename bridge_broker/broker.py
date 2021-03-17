import logging
import tornado.ioloop
import tornado.web

from bridge_broker.te_bridge import TEBridge
from bridge_broker.ce_bridge import CEBridge


class BridgeBroker:
    def __init__(self, sentry_mongo_uri, port):
        self.te_channels = {}

        self.app = tornado.web.Application([
            (r'/bridge/te', TEBridge, {'broker': self}),
            (r'/bridge/ce', CEBridge, {'broker': self}),
        ])
        self.app.listen(port)

        self.logger = logging.getLogger('bridge-broker')

    def run(self):
        self.logger.info(f'run')
        tornado.ioloop.IOLoop.current().start()

    async def on_te_onboard(self, te_id, te_channel):
        self.logger.info(f'te-id: {te_id}, channel: {te_channel}')
        self.te_channels[te_id] = te_channel
