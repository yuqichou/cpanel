# -*- coding: utf-8 -*-
'''
Created on Sep 21, 2012
@author: YuqiChou
'''
import pymongo
from cpanel import settings

'''
暂未找到好的集成办法
'''
def get_mongo_collection(collectionName):
    conn=pymongo.Connection(host=settings.MONGO_DB['HOST'],
                            port=settings.MONGO_DB['PORT'])
    db = conn[settings.MONGO_DB['NAME']]
    return db[collectionName]
