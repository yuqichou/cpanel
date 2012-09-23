# coding:utf8
from django.db import models

class App(models.Model):
    name = models.CharField('app名称',max_length=40)
    descript = models.CharField('描述',max_length=100,null=True)
    appid=models.CharField('APP_ID',max_length=40,unique=True)
    
    class Meta:  
        verbose_name = "App信息"  
        verbose_name_plural = "App信息"  
    
    def __unicode__(self):
        return self.name