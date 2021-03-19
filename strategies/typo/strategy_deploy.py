#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from decimal import Decimal
from typing import Dict, Tuple, Optional
from market.currency import *
from market.account import *


class StrategyDeploy:
    master_secret: Optional[AccountSecret]
    slave_secret: Optional[AccountSecret]

    master_reserve: Dict[MarketCurrency, Tuple[Decimal, Decimal]]
    slave_reserve: Dict[MarketCurrency, Tuple[Decimal, Decimal]]

    @staticmethod
    def load_from_dict(dictionary):
        strategy_deploy = StrategyDeploy()

        secret_master_id = dictionary['secret_master']
        secret_slave_id = dictionary['secret_slave']
        strategy_deploy.master_secret = secret_master_id
        strategy_deploy.slave_secret = secret_slave_id

        master_reserve = dictionary.get('master_reserve', None)
        slave_reserve = dictionary.get('master_reserve', None)
        if master_reserve is not None:
            strategy_deploy.master_reserve = StrategyDeploy.load_assets_reserve(master_reserve)
        if slave_reserve is not None:
            strategy_deploy.slave_reserve = StrategyDeploy.load_assets_reserve(slave_reserve)
        return strategy_deploy

    @staticmethod
    def load_assets_reserve(master_reserve):
        assets_reserve = {}
        for symbol, context in master_reserve.items():
            currency = MarketCurrency.create_from_raw_text_ic(symbol)
            reserve = (Decimal(context[0]), Decimal(context[1]))
            assets_reserve[currency] = reserve
        return assets_reserve
