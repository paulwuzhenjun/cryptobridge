#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from typing import Dict


def conj_influx_cosmetic(point: Dict, attachment=None, tags=None, fields=None):
    attachment = attachment if attachment is not None else {}
    tags = tags if tags is not None else {}
    fields = fields if fields is not None else {}

    point.update(attachment)
    point['tags'].update(tags)
    point['fields'].update(fields)
    return point
