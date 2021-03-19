import abc
import hmac
import base64
import hashlib
from typing import Optional
import pymongo
from core.datasource.mongo import *
from conj.mongo.strategy import *
from strategies.typo import *
from strategies.ce_bridge import *


class StrategyBase(abc.ABC):
    mongo_uri: str
    deploy_id: str
    bridge_broker_host: str
    bridge_broker_port: int

    mongo_clt: Optional[pymongo.MongoClient]
    strategy_deploy: Optional[StrategyDeploy]
    ce_bridge: Optional[CEBridge]

    def __init__(self, mongo_uri, deploy_id, bridge_broker_host, bridge_broker_port):
        self.mongo_uri, self.deploy_id = mongo_uri, deploy_id
        self.bridge_broker_host, self.bridge_broker_port = bridge_broker_host, bridge_broker_port

    async def initialize(self):
        self.mongo_clt = mongo_load_from_uri(self.mongo_uri)
        self.strategy_deploy = await self.__load_deploy(self.mongo_clt, self.deploy_id)
        # auth-code:
        secret_key = self.mongo_uri.encode()
        digest = hmac.new(secret_key, self.deploy_id.encode(), digestmod=hashlib.sha256).digest()
        auth_code = base64.b64encode(digest).decode()
        self.ce_bridge = CEBridge(self.bridge_broker_host, self.bridge_broker_port, self.deploy_id, auth_code)
        await self.ce_bridge.initialize()

    @staticmethod
    async def __load_deploy(mongo_clt, deploy_id):
        return await conj_strategy_load(mongo_clt, deploy_id)
