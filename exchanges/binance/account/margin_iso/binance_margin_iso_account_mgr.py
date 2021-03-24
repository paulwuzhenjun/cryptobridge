# from typing import *
# from decimal import Decimal
# from market.currency import *
# from market.account import *
# from market.position import *


# class BinanceMarginIsoAccountMgr(AccountManager):
#     def __init__(self, account_secret):
#         super().__init__(account_secret)
#         raise NotImplementedError()

#     async def fetch_asset(self, pair: MarketPair) -> List[AccountAsset]:
#         raise NotImplementedError()

#     async def fetch_position(self, pair: MarketPair) -> Dict[MarketPair, List[Position]]:
#         raise NotImplementedError()

#     async def borrow_asset(self, pair: MarketPair, currency: MarketCurrency, amount: Decimal):
#         raise NotImplementedError()

#     async def repay_asset(self, pair: MarketPair, currency: MarketCurrency, amount: Decimal):
#         raise NotImplementedError()


from binance.websockets import BinanceSocketManager
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
from binance.client import Client
client = Client('t3Y1TFkTQzyFDAaqizXUuCUDSvzsxJyWEQq2PaFkTB4nBTMQNr5iHxzMroS94szd',
                'A2Y8SbwN2623L3Lm8hGY3cG5EST7SrDyoJP0EhPrDjvgVRieWVWoBx5bSCpvqoD9', {"verify": False, "timeout": 20})


account = client.create_isolated_margin_account(base='BTC', quote='ETH')
info = client.get_isolated_margin_account()
print(f'info:{info}')

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something


bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()
