#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)


def conj_balance_load(mongo_client, balance_id):
    client, balance_id = balance_id.split('/')
    database = mongo_client['Sentry_Balance']
    coll = database[client]
    balance = coll.find_one({'_id': balance_id})
    return balance
