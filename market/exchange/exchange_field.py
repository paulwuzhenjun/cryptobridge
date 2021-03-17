from enum import Enum


class ExchangeField(Enum):
    SPOT = 'SPOT'
    MARGIN = 'MARGIN'
    SWAP = 'SWAP'
    FUTURES = 'FUTURES'
    FIAT = 'FIAT'

    @staticmethod
    def create_from_raw_text(text):
        return ExchangeField(text.upper())
