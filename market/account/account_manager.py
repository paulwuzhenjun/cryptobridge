import abc
import logging
from typing import Dict, List

from market.currency import *
from market.account.account_asset import AccountAsset
from market.account.account_secret import AccountSecret


class AccountManager(abc.ABC):
    account_secret: AccountSecret

    def __init__(self, account_secret):
        self.account_secret = account_secret
        self.logger = logging.getLogger('account-mgr')

    async def initialize(self):
        pass

    async def fetch_asset(self, pair: MarketPair) -> List[AccountAsset]:
        raise NotImplementedError()

    async def fetch_position(self, pair: MarketPair):
        raise NotImplementedError()

    async def transfer_asset(self, amount, currency, from_field, from_pair, to_field, to_pair):
        raise NotImplementedError()
