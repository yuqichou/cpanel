# -*- coding: utf-8 -*-
'''
Created on Sep 23, 2012
@author: YuqiChou
'''

DEFAULT_PAGE_SIZE=12

class Page():
    
#        self.pageSize = 20
#        self.firstPage = 1
#        self.gotoPage = 1
#
#        self.countPage=0
#        self.countData=0
#
#        self.lastPage=0
#        self.nextPage=0
#        self.prePage=0
#
#        self.hasNextPage = True
#        self.hasPrePage = True
    
    def __init__(self,gotoPage,countData,pageSize,data):
        
        self.data=data
        
        self.hasNextPage = True
        self.hasPrePage = True
        
        if (gotoPage < 1):
            gotoPage = 1
            
        if (pageSize < 1):
            pageSize = DEFAULT_PAGE_SIZE;
    
        self.gotoPage = gotoPage
        self.countData = countData
        self.pageSize = pageSize
        
        if (countData == 0):
            self.countPage = 1;
        
        if (countData % pageSize == 0):
            self.countPage = countData / pageSize;
        else:
            self.countPage = countData / pageSize + 1;
        
        self.lastPage = self.countPage;
        self.nextPage = self.gotoPage + 1;
        
        if (self.nextPage > self.countPage):
            self.hasNextPage = False;
            self.nextPage = self.countPage

            
        if (self.gotoPage > self.lastPage):
            self.prePage = self.lastPage
        else:
            self.prePage = self.gotoPage - 1;
            if (self.prePage < 1):
                self.hasPrePage = False;
                self.prePage = 1;
        
        

if __name__=='__main__':
    page=Page(gotoPage=2,countData=20,pageSize=DEFAULT_PAGE_SIZE,data=None)


