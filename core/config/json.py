#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import json
import jsmin


def conf_json_load_from_path(path):
    file = open(path, 'r')
    content = file.read()
    content_minified = jsmin.jsmin(content)
    return json.loads(content_minified)
