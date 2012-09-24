# coding:utf8
from db import mongo_util

'''
获取app models
'''
from bson.objectid import ObjectId
from db.page import Page, DEFAULT_PAGE_SIZE
import pymongo
def find_collections(appid):
    
    schemes=mongo_util.get_mongo_collection("scheme")
    
    appScheme=schemes.find_one({"app_id":appid})
    
    collections=list()
    
    if(appScheme!= None):
        for item in appScheme.get('models'):
            collections.append({
                                'display_name':item['display_name'],
                                'model_name':item['model_name'],
                                'app_id':appid,
                                })
    
    
    return collections

'''
获取model scheme
'''
def find_model_scheme(appid,model_name):
    schemes=mongo_util.get_mongo_collection("scheme")
    models=schemes.find_one({"app_id":appid}).get('models')
    
    tempModel=None
    for model in models:
        if not cmp(model_name,model.get('model_name')):
            tempModel=model
            break 
    
    return tempModel


'''
保存
'''
def save_model(app_id,model_name,saveObj):
    collection=mongo_util.get_mongo_collection(app_id+"_"+model_name)
    collection.insert(saveObj)

        
def find_models(app_id,model_name,**pageConfig):
    collection=mongo_util.get_mongo_collection(app_id+"_"+model_name)
    return collection.find()

def find_page_models(app_id,model_name,**pageConfig):
    
    gotoPage=pageConfig.get("gotoPage",1)
    pageSize=pageConfig.get("pageSize",DEFAULT_PAGE_SIZE)
    
    if gotoPage<0:
        gotoPage=1
    
    if pageSize<1:
        pageSize=DEFAULT_PAGE_SIZE
    
    collection=mongo_util.get_mongo_collection(app_id+"_"+model_name)
    data=collection.find(skip=(gotoPage-1)*pageSize,limit=pageSize).sort("_id", pymongo.DESCENDING)
    total=collection.count()
    return Page(gotoPage, total, pageSize, data)

def del_model(app_id,model_name,objid):
    collection=mongo_util.get_mongo_collection(app_id+"_"+model_name)
    collection.remove({"_id":ObjectId(str(objid))})
    
        

def find_model_data(app_id,model_name,objid):
    collection=mongo_util.get_mongo_collection(app_id+"_"+model_name)
    return collection.find_one({"_id":ObjectId(str(objid))})


def update_model(app_id,model_name,objid,updateDict):
    collection=mongo_util.get_mongo_collection(app_id+"_"+model_name)
    collection.update({"_id":ObjectId(str(objid))}, {"$set": updateDict})
    
    
    
    
    
    

