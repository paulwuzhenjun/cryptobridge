#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from influxdb import InfluxDBClient
from influxdb import DataFrameClient

from core.datasource.influx.influx_config import InfluxConfig


def influx_load_from_config(influx_config: InfluxConfig, is_data_frame=False):
    clazz = DataFrameClient if is_data_frame else InfluxDBClient
    return clazz(host=influx_config.host, port=influx_config.port,
                 username=influx_config.username, password=influx_config.password,
                 database=influx_config.default_database,
                 ssl=influx_config.ssl)
