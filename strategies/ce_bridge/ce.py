import ujson
import logging
import websockets


class CEBridge:
    bridge_broker_host: str
    bridge_broker_port: int
    te_id: str
    auth_code: str

    ws_stream: websockets.WebSocketClientProtocol

    def __init__(self, bridge_broker_host, bridge_broker_port, te_id, auth_code):
        self.bridge_broker_host = bridge_broker_host
        self.bridge_broker_port = bridge_broker_port
        self.te_id, self.auth_code = te_id, auth_code

        self.logger = logging.getLogger('ce-bridge')

    async def initialize(self):
        ws_uri = f'wss://{self.bridge_broker_host}:{self.bridge_broker_port}/bridge/ce'
        self.logger.info(f'te-id: {self.te_id}, ws-uri: {ws_uri}')
        self.ws_stream = await websockets.connect(ws_uri)
        # auth
        await self.post_ce_auth(self.te_id, self.auth_code)
        # connection
        await self.post_connection()
        # just poll
        await self.poll()

    async def poll(self):
        while True:
            message = await self.ws_stream.recv()
            self.logger.info(f'message: {message}')

    async def send_to_te(self, method, path, params):
        await self.ws_stream.send(ujson.dumps({
            'method': method, 'path': path, 'params': params
        }))

    async def post_connection(self):
        await self.ws_stream.send(ujson.dumps({
            'method': 'POST', 'path': '/ce/connection'
        }))

    async def post_ce_auth(self, te_id, auth_code):
        self.logger.info(f'te-id: {te_id}, auth-code: {auth_code}')
        await self.ws_stream.send(ujson.dumps({
            'method': 'POST', 'path': '/ce/auth', 'params': [te_id, auth_code]
        }))
