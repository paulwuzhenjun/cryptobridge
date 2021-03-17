import asyncio
import gate_api
from market.account import *
from market.exchange import *
from market.currency import *


class GateSpotAccountMgr(AccountManager):
    __std_field_to_ex_text_dict__ = {
        ExchangeField.SPOT: 'spot',
        ExchangeField.MARGIN: 'margin',
        ExchangeField.SWAP: 'futures',
        ExchangeField.FUTURES: 'delivery',
    }

    def __init__(self, account_secret):
        super().__init__(account_secret)

        self.conf = gate_api.Configuration()
        self.conf.key, self.conf.secret = account_secret.api_key, account_secret.api_secret

    async def transfer_asset(self, currency, amount, from_field, from_pair, to_field, to_pair):
        symbol = currency.value.upper()
        from_field_text = self.__std_field_to_ex_text_dict__[from_field]
        from_pair_text = from_pair.to_underscore_text()
        to_field_text = self.__std_field_to_ex_text_dict__[to_field]
        to_pair_text = to_pair.to_underscore_text()
        kwargs = {'currency': symbol, '_from': from_field_text, 'to': to_field_text, 'amount': str(amount)}
        if from_field == ExchangeField.MARGIN:
            kwargs['currency_pair'] = from_pair_text
        elif to_field == ExchangeField.MARGIN:
            kwargs['currency_pair'] = to_pair_text
        if currency == MarketCurrency.USDT:
            kwargs['settle'] = 'usdt'
        elif currency == MarketCurrency.BTC:
            kwargs['settle'] = 'btc'

        self.logger.info(f'kwargs: {kwargs}')

        wallet_rest = gate_api.WalletApi(gate_api.ApiClient(configuration=self.conf))
        transfer = gate_api.Transfer(**kwargs)
        response = await asyncio.get_event_loop().run_in_executor(None, wallet_rest.transfer, transfer)
        self.logger.info(f'response: {response}')
