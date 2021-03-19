import websockets


class CEBridge:
    bridge_broker_host: str
    bridge_broker_port: int

    ws_stream: websockets.WebSocketClientProtocol

    def __init__(self, bridge_broker_host, bridge_broker_port):
        self.bridge_broker_host = bridge_broker_host
        self.bridge_broker_port = bridge_broker_port

    async def initialize(self):
        ws_uri = f'wss://{self.bridge_broker_host}:{self.bridge_broker_port}/bridge/ce'
        self.ws_stream = await websockets.connect(ws_uri)

