FROM coinrising/cryptoforge-b_snap:v210314_10 AS b_snap

FROM python:3.7-buster

RUN pip3 install click simplejson jsonpickle requests websocket_client apscheduler requests_futures ecdsa
RUN pip3 install zmq python-dateutil pymongo aiohttp pyyaml pycryptodome influxdb pandas
RUN pip3 install dateparser bitmex broker-trade-client jsmin matplotlib kucoin-python ccxt
RUN pip3 install redis python-binance pycoingecko docker

RUN pip3 install git+https://github.com/gateio/gateapi-python.git

COPY --from=b_snap /opt/run_barrier_snapshot /opt/
COPY --from=b_snap /usr/lib/x86_64-linux-gnu /usr/lib/
COPY . /opt/cryptospace

WORKDIR /opt/cryptospace

