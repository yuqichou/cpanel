# -*- coding: utf-8 -*-
'''
Created on Sep 23, 2012
@author: YuqiChou
'''
from django import template
import datetime


register = template.Library()

'''
读取template动态属性
'''
@register.filter
def get_attr(value,arg):
    if(type(value)==dict):
        return value.get(arg)
    return ''


@register.filter
def get_date_attr(value,arg):
    if(type(value)==dict and type(value.get(arg))==datetime.datetime):
        return (str(value.get(arg).year)+"-"+str(value.get(arg).month)+"-"+str(value.get(arg).day))
    return ''


