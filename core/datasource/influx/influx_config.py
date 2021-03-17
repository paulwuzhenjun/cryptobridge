#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from __future__ import annotations

from core.config.json import conf_json_load_from_path


class InfluxConfig:
    host: str
    port: int
    username: str
    password: str

    default_database: str

    ssl: bool

    def __init__(self, host, port, username, password, default_database, ssl=False):
        self.host, self.port = host, port
        self.username, self.password = username, password
        self.default_database = default_database
        self.ssl = ssl

    @staticmethod
    def load_from_path(influx_config_path) -> InfluxConfig:
        conf = conf_json_load_from_path(influx_config_path)
        return InfluxConfig.load_from_json(conf)

    @staticmethod
    def load_from_json(conf):
        config = InfluxConfig(conf['host'], conf['port'], conf['username'], conf['password'], conf['database'], conf.get('ssl', False))
        return config
