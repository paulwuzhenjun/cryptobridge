#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from redis import StrictRedis

from core.datasource.redis.redis_config import RedisConfig


def redis_load_from_config(redis_config: RedisConfig):
    return StrictRedis(host=redis_config.host, port=redis_config.port, password=redis_config.password, db=redis_config.database)
