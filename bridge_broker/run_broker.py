import os
import sys
sys.path.append(os.getcwd())

import click
from core.logs import *
from bridge_broker.broker import BridgeBroker


@click.command()
@click.option('--port', help='the bridge-broker listen port', default=11011, required=True)
def run(port):
    logs_init_std('bridge-broker')

    port = port
    bridge_broker = BridgeBroker(port)
    bridge_broker.run()


if __name__ == '__main__':
    run()
