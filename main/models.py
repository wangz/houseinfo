#!/usr/bin/python
#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.db import models

# Create your models here.

TYPE_CHOICES= (('r','房源数'),('d','成交量'),('nc','新增客源'),('nh','新增房源'),('ns','带看量'),('mnc','月新增客源'),('mnh','月新增房源'),('mns','月带看量'),("td","历史总成交") )
CITY_CHOICES = (('bj','BeiJing'),('sh','ShangHai'))
class City(models.Model):  
    name = models.CharField(max_length=200)  
    def __unicode__(self):  
        return self.name  

class TotalPerDay(models.Model):  
    value = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now=True)  
    city = models.ForeignKey(City) 
    def __unicode__(self):  
        return self.value 

class MSummary(models.Model):
    value =  models.CharField(max_length=500,null=True)
    datetime =  models.DateField()
    city = models.CharField(max_length=20,choices=CITY_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.value

class Data(models.Model):
    city = models.CharField(max_length=20,choices=CITY_CHOICES)
    vtype =  models.CharField(max_length=20,choices=TYPE_CHOICES) 
    value = models.IntegerField()
    datetime =  models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    desc1 =  models.CharField(max_length=200,null=True)
    def __unicode__(self):
        return self.vtype + ' ' + str(self.value) + '         ' + str(self.created_at) 
     
