#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import logging
from core.datasource.mongo import *


def conj_mongo_load(mongo_client, mongo_id):
    logging.info(f'load mongo-id: {mongo_id}')
    col_name = mongo_id.split('@')[0]
    database = mongo_client['DataSource']
    coll = database[col_name]
    mongo_json = coll.find_one({'_id': mongo_id})
    return mongo_load_from_config(MongoConfig.load_from_json(mongo_json))
