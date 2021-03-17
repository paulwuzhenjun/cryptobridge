from market.account import *
from market.exchange import *
from exchanges.gate.account.spot.gate_spot_account_mgr import GateSpotAccountMgr


class ExchangeFactory:
    __account_mgr_dict__ = {
        ExchangeBrand.GATE: GateSpotAccountMgr
    }

    @staticmethod
    def create_account_mgr(secret: AccountSecret):
        try:
            clazz = ExchangeFactory.__account_mgr_dict__[secret.exchange]
        except KeyError:
            raise NotImplementedError(f'unsupported exchange: {secret.exchange}')
        return clazz(secret)
