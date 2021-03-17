from market.account import *
from market.exchange import *
from exchanges.binance import *
from exchanges.gate import *


class ExchangeFactory:
    __account_mgr_dict__ = {
        ExchangeBrand.BINANCE: {
            ExchangeField.SPOT: BinanceSpotAccountMgr
        },
        ExchangeBrand.GATE: {
            ExchangeField.SPOT: GateSpotAccountMgr
        }
    }

    @staticmethod
    def create_account_mgr(secret: AccountSecret):
        try:
            clazz = ExchangeFactory.__account_mgr_dict__[secret.exchange][secret.field]
        except KeyError:
            raise NotImplementedError(f'unsupported exchange({secret.exchange})@field({secret.field})')
        return clazz(secret)
