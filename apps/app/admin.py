# -*- coding: utf-8 -*-
'''
Created on Sep 23, 2012
@author: YuqiChou
'''
from apps.app.models import App
from django.contrib import admin

class AppAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('name', 'descript','appid')
    search_fields = ['name', 'descript','appid']
    list_filter = ['name','appid']
    
    
admin.site.register(App, AppAdmin)