from typing import *
from market.account import *
from market.currency import *
from strategies.base import *
from strategies.typo import *


class StrategyCX(StrategyBase):
    master_account_secret: AccountSecret
    slave_account_secret: AccountSecret

    master_account_mgr: AccountManager
    slave_account_mgr: AccountManager

    def __init__(self, mongo_uri, deploy_id, bridge_broker_host, bridge_broker_port):
        super().__init__(mongo_uri, deploy_id, bridge_broker_host, bridge_broker_port)

    async def initialize(self):
        await super().initialize()

    async def te_get_pair_allowence(self, pair):
        """
        获取交易对的允许位
        """
        raise NotImplementedError()

    async def te_set_pair_allowence(self, pair, allowence):
        """
         设置交易对的允许位
        """
        raise NotImplementedError()

    async def te_get_spreads(self) -> Dict[MarketPair, SpreadArb]:
        """
        获取当前spreads
        """
        raise NotImplementedError()

    async def te_set_spreads(self, spreads: Dict[MarketPair, SpreadArb]):
        """
        设置当前spreads
        """
        spreads_json = spreads
        await self.ce_bridge.send_to_te('POST', '/ce/te/cx/params', {
            'spreads': spreads_json
        })
