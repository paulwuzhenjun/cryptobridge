FROM python:3.7-buster

COPY . /opt/cryptobridge

RUN pip3 install -r /opt/cryptobridge/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

WORKDIR /opt/cryptobridge

