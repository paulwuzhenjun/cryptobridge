import abc
import logging
from decimal import Decimal
from typing import Dict, List

from market.currency import *
from market.account import *
from market.position import *


class AccountManager(abc.ABC):
    account_secret: AccountSecret

    def __init__(self, account_secret):
        self.account_secret = account_secret
        self.logger = logging.getLogger('account-mgr')

    async def initialize(self):
        pass

    async def fetch_asset(self, pair: MarketPair) -> List[AccountAsset]:
        raise NotImplementedError()

    async def fetch_position(self, pair: MarketPair) -> Dict[MarketPair, List[Position]]:
        raise NotImplementedError()

    async def borrow_asset(self, pair: MarketPair, currency: MarketCurrency, amount: Decimal):
        raise NotImplementedError()

    async def repay_asset(self, pair: MarketPair, currency: MarketCurrency, amount: Decimal):
        raise NotImplementedError()

    async def transfer_asset(self, amount, currency, from_field, from_pair, to_field, to_pair):
        raise NotImplementedError()
