# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2012
@author: YuqiChou
'''
from db.page import DEFAULT_PAGE_SIZE

def global_list_per_page(context):
    return {'GLOBAL_LIST_PER_PAGE': DEFAULT_PAGE_SIZE}