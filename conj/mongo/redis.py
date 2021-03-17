#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import logging
from core.datasource.redis import *


def conj_redis_load(mongo_client, redis_id):
    logging.info(f'load redis-id: {redis_id}')
    col_name = redis_id.split('@')[0]
    database = mongo_client['DataSource']
    coll = database[col_name]
    influx_json = coll.find_one({'_id': redis_id})
    return redis_load_from_config(RedisConfig.load_from_json(influx_json))
