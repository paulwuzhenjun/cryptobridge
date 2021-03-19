class StrategyBase:
    deploy_id: str

    def __init__(self, deploy_id):
        self.deploy_id = deploy_id

        self.ce_bridge = None

    async def initialize(self):

    async def __load_deploy(self, deploy):
