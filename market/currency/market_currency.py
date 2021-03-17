#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from __future__ import annotations
from enum import Enum


class MarketCurrency(Enum):
    _1INCH = '1INCH'

    AAVE = 'AAVE'
    ADA = 'ADA'
    ALPHA = 'ALPHA'
    ALGO = 'ALGO'
    ALT = 'ALT'
    AR = 'AR'
    ATOM = 'ATOM'

    BAND = 'BAND'
    BAT = 'BAT'
    BCH = 'BCH'
    BCHABC = 'BCHABC'
    BNB = 'BNB'
    BNT = 'BNT'
    BSV = 'BSV'
    BTC = 'BTC'
    BUSD = 'BUSD'

    CNY = 'CNY'
    COMP = 'COMP'
    CRV = 'CRV'

    DASH = 'DASH'
    DOGE = 'DOGE'
    DOT = 'DOT'

    EGT = 'EGT'
    EOS = 'EOS'
    ETC = 'ETC'
    ETH = 'ETH'

    FIL = 'FIL'
    FIL6 = 'FIL6'
    FLM = 'FLM'

    GRT = 'GRT'
    GT = 'GT'

    HT = 'HT'
    HUSD = 'HUSD'

    IOST = 'IOST'
    IOTA = 'IOTA'

    KAN = 'KAN'
    KAVA = 'KAVA'
    KSM = 'KSM'

    LEND = 'LEND'
    LINK = 'LINK'
    LRC = 'LRC'
    LTC = 'LTC'

    MATIC = 'MATIC'

    NEO = 'NEO'

    OKB = 'OKB'
    ONT = 'ONT'
    OMG = 'OMG'

    RVN = 'RVN'

    SUSHI = 'SUSHI'

    TRX = 'TRX'

    QTUM = 'QTUM'

    UNFI = 'UNFI'
    UNI = 'UNI'
    USD = 'USD'
    USDC = 'USDC'
    USDK = 'USDK'
    USDT = 'USDT'

    VET = 'VET'

    XLM = 'XLM'
    XMR = 'XMR'
    XRP = 'XRP'
    XTZ = 'XTZ'
    XVS = 'XVS'

    ZEC = 'ZEC'

    WAVES = 'WAVES'
    YFI = 'YFI'
    YFII = 'YFII'
    ZIL = 'ZIL'
    AVAX = 'AVAX'
    EGLD = 'EGLD'
    ENJ = 'ENJ'
    FTM = 'FTM'
    LUNA = 'LUNA'
    MKR = 'MKR'
    NEAR = 'NEAR'
    REN = 'REN'
    RSR = 'RSR'
    RUNE = 'RUNE'
    SNX = 'SNX'
    SOL = 'SOL'
    SRM = 'SRM'
    LINCH = 'LINCH'
    SXP = 'SXP'
    ZRX = 'ZRX'
    TOMO = 'TOMO'

    @staticmethod
    def create_from_raw_text_ic(text):
        text_uc = text.upper()
        if text == 'XBT':
            text_uc = 'BTC'
        return MarketCurrency(text_uc)
