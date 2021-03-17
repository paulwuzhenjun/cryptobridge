#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from __future__ import annotations
from market.currency.market_currency import MarketCurrency


class MarketPair:
    def __init__(self, base: [MarketCurrency], quote: [MarketCurrency], period=''):
        self.base = base
        self.quote = quote
        self.period = period

    @staticmethod
    def create_from_strike_text_ic(symbol, is_raise=True):
        """
        btc-usd-{period}
        """
        return MarketPair.__create_from_sep_text(symbol.lower(), '-', is_raise)

    @staticmethod
    def create_from_underscore_text_ic(symbol: str, is_raise=True):
        """
        btc_usd
        """
        return MarketPair.__create_from_sep_text(symbol.lower(), '_', is_raise)

    @staticmethod
    def create_from_dense_text_ic(text: str, is_raise=True):
        """
        btcusdt
        """
        symbolic_assets = ["xbt", "btc", "eth", 'bnb',
                           "busd", "husd", "usdt", 'usdc', "usd", 'pax', 'bkrw', 'bidr', 'aud'
                           "okb", "ht", "gt", 'xrp', 'trx']

        text = text.lower()
        for keyword in symbolic_assets:
            index = text.find(keyword)
            if index == -1:
                continue
            if index != 0 and index + len(keyword) != len(text):    # 解决 dashusdt 命中 husd
                continue
            base, quote = None, None
            try:
                if index == 0:
                    base = MarketCurrency.create_from_raw_text_ic(keyword)
                    quote = MarketCurrency.create_from_raw_text_ic(text[len(keyword):])
                else:
                    quote = MarketCurrency.create_from_raw_text_ic(keyword)
                    base = MarketCurrency.create_from_raw_text_ic(text[:index])
            except ValueError:
                if is_raise:
                    raise
            return MarketPair(base, quote)
        else:
            if is_raise:
                raise ValueError("decode failed: {}".format(text))

    @staticmethod
    def __create_from_sep_text(symbol: str, sep: str, is_raise):
        parts = symbol.split(sep)
        if len(parts) == 2:
            parts.append('')
        base, quote = None, None
        try:
            base = MarketCurrency.create_from_raw_text_ic(parts[0])
            quote = MarketCurrency.create_from_raw_text_ic(parts[1])
        except ValueError:
            if is_raise:
                raise
        return MarketPair(base, quote, parts[2])

    def to_dense_text(self):
        return self.__to_text('')

    def to_strike_text(self):
        return self.__to_text('-')

    def to_slash_text(self):
        return self.__to_text('/')

    def to_underscore_text(self):
        return self.__to_text('_')

    def __to_text(self, sep: str):
        base_symbol = 'none' if self.base is None else self.base.value.lower()
        quote_symbol = 'none' if self.quote is None else self.quote.value.lower()
        parts = [base_symbol, quote_symbol]
        if len(self.period) != 0:
            parts.append(self.period)
        return sep.join(parts)

    def __repr__(self):
        return self.to_strike_text()

    def __eq__(self, o: MarketPair) -> bool:
        return self.base == o.base and self.quote == o.quote and self.period == o.period

    def __hash__(self) -> int:
        return hash(self.base) + hash(self.quote) + hash(self.period)
