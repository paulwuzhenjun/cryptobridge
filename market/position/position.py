#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import time
import ujson
from decimal import Decimal

from market.currency import *


class Position:
    pair: MarketPair
    milli: int
    long: Decimal
    long_avg_price: Decimal
    short: Decimal
    short_avg_price: Decimal
    bankrupt_price: Decimal

    def __init__(self, pair, milli=int(time.time()*1000),
                 long=Decimal(0), long_avg_price=Decimal(0),
                 short=Decimal(0), short_avg_price=Decimal(0), bankrupt_price=Decimal(0)):
        self.pair = pair
        self.milli = milli
        self.long, self.long_avg_price = long, long_avg_price
        self.short, self.short_avg_price = short, short_avg_price
        self.bankrupt_price = bankrupt_price

    def stringify(self):
        return ujson.dumps(self.__dict__, default=lambda pair: str(pair))

    def __repr__(self):
        return self.stringify()
