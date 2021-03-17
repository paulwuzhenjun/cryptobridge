import asyncio
import functools
from binance import client
from market.account import *
from market.exchange import *
from market.currency import *


class BinanceSpotAccountMgr(AccountManager):
    def __init__(self, account_secret):
        super().__init__(account_secret)

        self.rest_clt = client.Client(api_key=self.account_secret.api_key, api_secret=self.account_secret.api_secret)

    async def transfer_asset(self, currency, amount, from_field, from_pair, to_field, to_pair):
        symbol = currency.value.upper()
        from_field_text = self.__std_field_to_ex_text__(from_field, from_pair.quote)
        to_field_text = self.__std_field_to_ex_text__(to_field, to_pair.quote)
        kwargs = {
            'type': f'{from_field_text}_{to_field_text}',
            'asset': symbol,
            'amount': str(amount)
        }

        self.logger.info(f'kwargs: {kwargs}')

        await asyncio.get_event_loop().run_in_executor(None, functools.partial(self.rest_clt.universal_transfer, **kwargs))

    def __std_field_to_ex_text__(self, field, settlement):
        if field == ExchangeField.SPOT:
            return 'MAIN'
        elif field == ExchangeField.MARGIN:
            return 'MARGIN'
        elif field == ExchangeField.SWAP or field == ExchangeField.FUTURES:
            if settlement == MarketCurrency.USDT:
                return 'UMFUTURE'
            elif settlement == MarketCurrency.USD:
                return 'CMFUTURE'
        raise NotImplementedError()
