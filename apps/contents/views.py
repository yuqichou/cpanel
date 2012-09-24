# coding:utf8
from apps.app.models import App
from apps.contents.models import find_collections, find_model_scheme, \
    find_page_models, save_model, del_model, find_model_data, update_model
from cpanel import settings
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
import datetime
import os
import time
import uuid

def main_page(request):
    return render_to_response('main.html',context_instance=RequestContext(request))

def top_page(request):
    #需要获取用户信息
    return render_to_response('include/includeTopNav.html',context_instance=RequestContext(request))

def left_catalogues(request):
    
    
    appDict=dict()
    for item in App.objects.all():
        try:
            appDict[item.name]=find_collections(item.appid)
        except Exception,e:
            print(e)
            pass
        
    return render_to_response('leftMenu.html',
                              {'appDict':appDict},
                              context_instance=RequestContext(request))
    

'''
查询
'''
def view_page(request,app_id,model_name):
    modelScheme=find_model_scheme(app_id, model_name)
    
    list_display=modelScheme.get('list_display',list())
    fields=modelScheme.get('fields')
    
    modelDict={'app_id':app_id,
               'model_name':model_name,
               'fields':modelScheme.get('fields')}
    
    ##需要显示的字段
    displays=list()
    for field_display in list_display:
        for field in fields:
            if(field_display in field['field_name']):
                displays.append(field['display_name'])
                
    gotoPage = request.GET.get('gotoPage')
    pageSize = request.GET.get('pageSize')
    if(gotoPage!=None):
        gotoPage=int(gotoPage)
    if(pageSize!=None):
        pageSize=int(pageSize)
        
    
    page=find_page_models(app_id, model_name,gotoPage=gotoPage,pageSize=pageSize)
    models=page.data
    
    modelDict['displays']=displays
    modelDict['list_data']=models
    modelDict['list_display']=list_display
    modelDict['page']=page
    
    
    return render_to_response('content_list.html',
                              modelDict,
                              context_instance=RequestContext(request))

'''
添加页面
'''
def add_page(request,app_id,model_name):
    modelScheme=find_model_scheme(app_id, model_name)
    return render_to_response('content_add.html',
                              {'app_id':app_id,
                               'fields':modelScheme['fields'],
                               'model_name':model_name,
                               'model_display_name':modelScheme['display_name']},
                              context_instance=RequestContext(request))
    
'''
保存
'''
def save_model_data(request,app_id,model_name):
    modelScheme=find_model_scheme(app_id, model_name)
    fields=modelScheme['fields']
    saveObj=dict()
    for field in fields:
        fieldValue=request.POST.get(field['field_name'])
        fieldValue=__handle_field__(fieldValue,field,request)
        
            
        saveObj[field['field_name']]=fieldValue
    save_model(app_id,model_name,saveObj)
        
    messages.add_message(request, messages.INFO, '添加成功')
    return redirect('apps.contents.views.view_page', app_id=app_id,model_name=model_name)

'''
删除
'''
def del_model_data(request,app_id,model_name,objid):
    del_model(app_id,model_name,objid)
    messages.add_message(request, messages.INFO, '删除成功')
    return redirect('apps.contents.views.view_page', app_id=app_id,model_name=model_name)
    
'''
编辑页面
'''
def edit_page(request,app_id,model_name,objid):
    modelScheme=find_model_scheme(app_id, model_name)
    model=find_model_data(app_id,model_name,objid)
    
    return render_to_response('content_edit.html',
                              {'model':model,
                               'app_id':app_id,
                               'fields':modelScheme['fields'],
                               'model_name':model_name,
                               'model_display_name':modelScheme['display_name']},
                               context_instance=RequestContext(request))


def update_model_data(request,app_id,model_name,objid):
    modelScheme=find_model_scheme(app_id, model_name)
    fields=modelScheme['fields']
    updateObj=dict()
    for field in fields:
        fieldValue=request.POST.get(field['field_name'])
        fieldValue=__handle_field__(fieldValue,field,request)
        updateObj[field['field_name']]=fieldValue
        
    update_model(app_id,model_name,objid,updateObj)
        
    messages.add_message(request, messages.INFO, '修改成功')
    return redirect('apps.contents.views.edit_page', app_id=app_id,model_name=model_name,objid=objid)
    
    
    
def __handle_field__(fieldValue,field,request):
    if(fieldValue!=None):
        if('BooleanField' in field['field_type']):
            if(fieldValue=='1'):
                fieldValue=True
            elif(fieldValue=='0'):
                    fieldValue=False
        elif('DateField' in field['field_type']):
            try:
                date=time.strptime(fieldValue, "%Y-%m-%d")
                fieldValue=datetime.datetime(date[0], date[1],date[2])
            except Exception:
                pass
        elif('IntegerField' in field['field_type']):
            try:
                fieldValue=int(fieldValue)
            except Exception:
                pass
            
    if('FileField' in field['field_type']):
        try:
            uploadFile = request.FILES.get(field['field_name'])
            fieldValue=request.POST.get(field['field_name']+"_path_value")
            if(uploadFile!=None):
                datePath=time.strftime("%Y/%m/%d/", time.localtime())
                savePath=settings.MEDIA_ROOT+datePath
                fileName=str(uuid.uuid1())+"."+uploadFile.name.split(".")[-1]
                
                if(not os.path.exists(savePath)):
                    os.makedirs(savePath)
                    
                destination = open((savePath+fileName), 'wb+')
                for chunk in uploadFile.chunks():
                    destination.write(chunk)
                destination.close()
                    
                fieldValue=settings.MEDIA_URL+datePath+fileName
        except Exception,e:
            print(e)
            pass    
        
    return fieldValue