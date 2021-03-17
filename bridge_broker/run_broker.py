import os
import sys
sys.path.append(os.getcwd())

import click
from core.logs import *
from bridge_broker.broker import BridgeBroker


@click.command()
@click.option('--sentry', help='the sentry mongo-uri', required=True)
@click.option('--port', help='the bridge-broker listen port', default=11011, required=True)
def run(sentry, port):
    logs_init_std('bridge-broker')

    sentry_mongo_uri, port = sentry, port
    bridge_broker = BridgeBroker(sentry_mongo_uri, port)
    bridge_broker.run()


if __name__ == '__main__':
    run()
