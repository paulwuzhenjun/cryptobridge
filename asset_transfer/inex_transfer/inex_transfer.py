import asyncio
from decimal import Decimal
from market.currency import *
from market.exchange import *
from market.account import *
from core.datasource.mongo import *
from conj.mongo.secret import *
from exchanges.factory import *


class InexTransfer:
    mongo_uri: str
    secret_id: str
    currency: MarketCurrency
    amount: Decimal
    from_field: ExchangeField
    from_pair: MarketPair
    to_field: ExchangeField
    to_pair: MarketPair

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.currency = MarketCurrency.create_from_raw_text_ic(self.currency)
        self.amount = Decimal(self.amount)
        self.from_field = ExchangeField.create_from_raw_text(self.from_field)
        self.from_pair = MarketPair.create_from_strike_text_ic(self.from_pair)
        self.to_field = ExchangeField.create_from_raw_text(self.to_field)
        self.to_pair = MarketPair.create_from_strike_text_ic(self.to_pair)

    def transfer(self):
        mongo_clt = mongo_load_from_uri(self.mongo_uri)
        secret: AccountSecret = conj_secret_load(mongo_clt, self.secret_id)
        account_mgr = ExchangeFactory.create_account_mgr(secret)
        asyncio.run(account_mgr.transfer_asset(self.currency, self.amount, self.from_field, self.from_pair, self.to_field, self.to_pair))
