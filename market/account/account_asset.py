#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import simplejson
from decimal import Decimal

from market.currency.market_currency import MarketCurrency


class AccountAsset:
    currency: MarketCurrency
    available: Decimal
    freeze: Decimal
    debt: Decimal
    interest: Decimal

    def __init__(self, currency, available, freeze=Decimal(0), debt=Decimal(0), interest=Decimal(0)):
        self.currency, self.available, self.freeze, self.debt, self.interest = currency, available, freeze, debt, interest

    def equity(self):
        return self.available + self.freeze + self.debt + self.interest

    def stringify(self):
        return simplejson.dumps(self.__dict__, default=lambda o: str(o))

    def __repr__(self):
        return self.stringify()
