import os
import sys
sys.path.append(os.getcwd())

import click
import asyncio
from core.logs import *
from bridge_broker.broker import BridgeBroker


@click.command()
@click.option('--sentry', help='the sentry mongo-uri', required=True)
@click.option('--port', help='the bridge-broker listen port', default=11011, required=True)
def run(sentry, port):
    logs_init_std('bridge-broker')

    mongo_uri = sentry
    port = port
    bridge_broker = BridgeBroker(mongo_uri, port)
    bridge_broker.run()


if __name__ == '__main__':
    run()
