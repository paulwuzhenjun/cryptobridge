#!/usr/bin/env python3                                                                               
# -*- coding: utf-8 -*-                                                                              
# @author: zig(zig@uranome.com)

from conj.mongo.secret import conj_secret_load
from strategies.typo import *


async def conj_strategy_load(mongo_client, strategy_id):
    deploy_client = strategy_id.split('@')[0]
    deploy_database = mongo_client['Strategy_deploy']
    deploy_coll = deploy_database[deploy_client]
    deploy_doc = deploy_coll.find_one({'_id': strategy_id})
    template_doc = {}
    # template
    if '@template' in deploy_doc:
        template_id = deploy_doc['@template']
        template_coll = template_id.split('@')[-1]
        template_database = mongo_client['Strategy_template']
        template_coll = template_database[template_coll]
        template_doc = template_coll.find_one({'_id': template_id})
    final_doc = template_doc
    final_doc.update(deploy_doc)

    strategy_deploy_inst = StrategyDeploy.load_from_dict(final_doc)
    strategy_deploy_inst.master_secret = conj_secret_load(mongo_client, strategy_deploy_inst.master_secret)
    strategy_deploy_inst.slave_secret = conj_secret_load(mongo_client, strategy_deploy_inst.slave_secret)
    return strategy_deploy_inst
