#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from market.account.account_secret import AccountSecret


def conj_secret_load(mongo_client, secret_id):
    client, secret_id = secret_id.split('/')
    database = mongo_client['Secrets']
    coll = database[client]
    secret = coll.find_one({'_id': secret_id})
    return AccountSecret.load_from_dict(secret)
