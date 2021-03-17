#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

import json
import tornado.websocket


class CEBridge(tornado.websocket.WebSocketHandler):
    async def on_message(self, message):
        message_json = json.loads(message)
