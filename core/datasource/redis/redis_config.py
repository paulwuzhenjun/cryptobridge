#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from __future__ import annotations

from core.config.json import conf_json_load_from_path


class RedisConfig:
    host: str
    port: int
    password: str
    database: int

    def __init__(self, host, port, password, database=0):
        self.host, self.port, self.password, self.database = host, port, password, database

    @staticmethod
    def load_from_path(influx_config_path) -> RedisConfig:
        conf = conf_json_load_from_path(influx_config_path)
        return RedisConfig.load_from_json(conf)

    @staticmethod
    def load_from_json(conf) -> RedisConfig:
        config = RedisConfig(conf['host'], int(conf['port']), conf['password'], conf.get('database', 0))
        return config
