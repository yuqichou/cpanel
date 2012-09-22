# coding:utf8
from db import mongo_util

'''
获取app models
'''
def find_collections(appid):
    
    schemes=mongo_util.get_mongo_collection("scheme")
    
    appScheme=schemes.find_one({"app_id":appid})
    
    collections=list()
    
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
        
        
        
    
