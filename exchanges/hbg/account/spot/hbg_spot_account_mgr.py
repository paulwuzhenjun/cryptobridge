from exchanges.hbg.utils import *
from market.account import *
from market.exchange import *


class HBGSpotAccountMgr(AccountManager):
    def __init__(self, account_secret):
        super().__init__(account_secret)

    async def transfer_asset(self, currency, amount, from_field, from_pair, to_field, to_pair):
        if from_field == ExchangeField.SWAP or to_field == ExchangeField.SWAP:
            await self.__transfer_between_spot_swap(currency, amount, from_field, to_field)

    async def __transfer_between_spot_swap(self, currency, amount, from_field, to_field):
        uri = 'https://api.huobi.pro/v2/account/transfer'
        kwargs = {
            'from': from_field.value.lower(), 'to': to_field.value.lower(),
            'currency': currency.value, 'amount': amount
        }

        self.logger.info(f'kwargs: {kwargs}')

        response = await hbg_contracts_post(self.account_secret.api_key, self.account_secret.api_secret, uri, kwargs)
        self.logger.info(f'response: {response}')
