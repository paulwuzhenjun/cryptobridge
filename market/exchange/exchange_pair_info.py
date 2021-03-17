#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import simplejson
from decimal import Decimal

from market.currency.market_pair import MarketPair


class ExchangePairInfo:
    pair: MarketPair
    step_size_base: Decimal
    step_size_quote: Decimal
    min_size_base: Decimal
    min_size_quote: Decimal

    def __init__(self, pair, step_size_base, step_size_quote, min_size_base, min_size_quote):
        self.pair = pair
        self.step_size_base, self.step_size_quote = step_size_base, step_size_quote
        self.min_size_base, self.min_size_quote = min_size_base, min_size_quote

    def stringify(self):
        return simplejson.dumps(self.__dict__, default=lambda o: str(o))

    def __repr__(self):
        return self.stringify()
