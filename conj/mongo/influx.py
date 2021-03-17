#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import logging
from core.datasource.influx import *


def conj_influx_load(mongo_client, influx_id):
    logging.info(f'load influx-id: {influx_id}')
    col_name = influx_id.split('@')[0]
    database = mongo_client['DataSource']
    coll = database[col_name]
    influx_json = coll.find_one({'_id': influx_id})
    return influx_load_from_config(InfluxConfig.load_from_json(influx_json))
