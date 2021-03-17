from enum import Enum


class ExchangeBrand(Enum):
    BINANCE = 'BINANCE'
    BITMEX = 'BITMEX'
    BYBIT = 'BYBIT'
    GATE = 'GATE'
    HBG = 'HBG'
    HBTC = 'HBTC'
    HOTBIT = 'HOTBIT'
    OKEX = 'OKEX"'
    ZB = 'ZB'

    @staticmethod
    def create_from_raw_text(text: str):
        return ExchangeBrand(text.upper())
