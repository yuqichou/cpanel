# -*- coding: utf-8 -*-
'''
Created on Sep 23, 2012
@author: YuqiChou
'''
from django import template


register = template.Library()

'''
template无法取
'''
@register.filter
def get_underscores_attr(value,arg):
    if(type(value)==dict):
        return value.get(arg)

