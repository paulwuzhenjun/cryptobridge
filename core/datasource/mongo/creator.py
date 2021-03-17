#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from pymongo import MongoClient

from core.datasource.mongo.mongo_config import MongoConfig


def mongo_load_from_uri(mongo_uri):
    return MongoClient(host=mongo_uri)


def mongo_load_from_config(mongo_config: MongoConfig):
    return MongoClient(host=mongo_config.host, port=mongo_config.port,
                       username=mongo_config.username, password=mongo_config.password)
