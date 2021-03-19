from strategies.base import *


class StrategyCX(StrategyBase):
    def __init__(self, deploy_id):
        super().__init__(deploy_id)

    async def initialize(self):

