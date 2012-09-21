# coding:utf8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.app.models import App
from apps.contents.models import find_collections, find_model_scheme

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
        except Exception:
            pass
        
    return render_to_response('leftMenu.html',
                              {'appDict':appDict},
                              context_instance=RequestContext(request))
    


def view_page(request,app_id,model_name):
    
    
    modelScheme=find_model_scheme(app_id, model_name)
    
    fields=modelScheme['fields']
    
    for i in fields:
        print(i['display_name'])
    
    return render_to_response('content_list.html',
                              {'fields':None,
                               'list_data':None},
                              context_instance=RequestContext(request))






