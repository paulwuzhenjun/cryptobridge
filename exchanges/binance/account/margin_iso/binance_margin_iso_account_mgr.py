from typing import *
from decimal import Decimal
from market.currency import *
from market.account import *
from market.position import *


class BinanceMarginIsoAccountMgr(AccountManager):
    def __init__(self, account_secret):
        super().__init__(account_secret)
        raise NotImplementedError()

    async def fetch_asset(self, pair: MarketPair) -> List[AccountAsset]:
        raise NotImplementedError()

    async def fetch_position(self, pair: MarketPair) -> Dict[MarketPair, List[Position]]:
        raise NotImplementedError()

    async def borrow_asset(self, pair: MarketPair, currency: MarketCurrency, amount: Decimal):
        raise NotImplementedError()

    async def repay_asset(self, pair: MarketPair, currency: MarketCurrency, amount: Decimal):
        raise NotImplementedError()
