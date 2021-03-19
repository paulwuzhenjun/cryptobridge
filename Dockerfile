FROM python:3.7-buster

COPY . /opt/cryptobridge

RUN pip3 install click==7.1.2 jsmin==2.2.2 pymongo==3.11.3 simplejson==3.17.2 tornado==6.1
RUN pip3 install broker-trade-client aiohttp[speedups] websockets ujson
RUN pip3 install git+https://github.com/coinrising/python-binance.git@0.7.10
RUN pip3 install git+https://github.com/gateio/gateapi-python.git@4.19.4
RUN pip3 install git+https://github.com/HuobiRDCenter/huobi_Python.git@v2.3.0

WORKDIR /opt/cryptobridge

