#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from influxdb.client import InfluxDBClient
from influxdb.resultset import ResultSet


async def influx_fetch_limit_1(influx_clt: InfluxDBClient, measurement, is_near_now: bool, database=None):
    sql = f"SELECT * FROM {measurement} ORDER BY time {'DESC' if is_near_now else 'ASC'} LIMIT 1"
    rs: ResultSet = influx_clt.query(sql)
    points = list(rs.get_points(measurement))
    if len(points) == 1:
        return points[-1]
