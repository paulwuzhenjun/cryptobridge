from strategies.base import *


class StrategyCX(StrategyBase):
    def __init__(self, mongo_uri, deploy_id, bridge_broker_host, bridge_broker_port):
        super().__init__(mongo_uri, deploy_id, bridge_broker_host, bridge_broker_port)

    async def initialize(self):
        await super().initialize()
