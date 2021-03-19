import ujson
import asyncio
import aiohttp
from typing import Optional

__aio_session__: Optional[aiohttp.ClientSession] = None


async def get_aio_session():
    global __aio_session__

    if __aio_session__ is None:
        __aio_session__ = aiohttp.ClientSession(json_serialize=ujson.dumps)
    return __aio_session__


async def close_aio_session():
    if __aio_session__ is not None:
        await __aio_session__.close()
