#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from __future__ import annotations
import simplejson
from decimal import Decimal
from core.config.json import conf_json_load_from_path

from market.exchange.exchange_brand import ExchangeBrand
from market.exchange.exchange_field import ExchangeField
from market.currency.market_currency import MarketCurrency


class AccountSecret:
    api_key: str
    api_secret: str
    api_phrase: str

    client: str
    username: str
    exchange: ExchangeBrand
    field: ExchangeField
    settlement: MarketCurrency

    maker_fee_rebate: Decimal
    taker_fee_rebate: Decimal
    fee_type: str

    def __str__(self):
        return simplejson.dumps(self.__dict__, default=lambda o: str(o))

    @staticmethod
    def load_from_path(secret_path) -> AccountSecret:
        secret_dict = conf_json_load_from_path(secret_path)
        return AccountSecret.load_from_dict(secret_dict)

    @staticmethod
    def load_from_dict(secret_dict) -> AccountSecret:
        account_secret = AccountSecret()
        account_secret.api_key = secret_dict['apikey']
        account_secret.api_secret = secret_dict['secretkey']
        account_secret.api_phrase = secret_dict.get('passphrase', '')
        account_secret.client = secret_dict['client']
        account_secret.username = secret_dict['username']
        account_secret.exchange = ExchangeBrand.create_from_raw_text(secret_dict['exchange'])
        account_secret.field = ExchangeField.create_from_raw_text(secret_dict['field'])
        settlement_symbol = secret_dict.get('settlement')
        if settlement_symbol is not None:
            account_secret.settlement = MarketCurrency.create_from_raw_text_ic(settlement_symbol)
        maker_fee_rebate, taker_fee_rebate, fee_type = secret_dict.get('maker_fee_rebate'), secret_dict.get('taker_fee_rebate'),  secret_dict.get('fee_type')
        if maker_fee_rebate is not None:
            account_secret.maker_fee_rebate = Decimal(maker_fee_rebate)
        if taker_fee_rebate is not None:
            account_secret.taker_fee_rebate = Decimal(taker_fee_rebate)
        if fee_type is not None:
            account_secret.fee_type = fee_type
        return account_secret
