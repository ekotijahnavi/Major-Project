# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Abstracts(models.Model):  
    name = models.CharField(max_length=50,default='',null=False)  
    
    email = models.EmailField(max_length=50,default='',null=False)  
    project = models.CharField(max_length=50,default='',null=False)  
    abstract = models.TextField(max_length=1000,default='',null=False)   
class Eceabstract(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)   
class Cseab(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)   
class Civilabstract(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)  
class Mechabstract(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)   
class FeedBack(models.Model):
    Name = models.CharField(max_length=50,default='',null=False)
    Email = models.EmailField(max_length=50,default='',null=False)
    feedback = models.TextField(max_length=1000,default='',null=False)
class Contact(models.Model):
    Name = models.CharField(max_length=50,default='',null=False)
    Email = models.EmailField(max_length=50,default='',null=False)
    Message = models.TextField(max_length=1000,default='',null=False)
class Cseproject(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)  
class Eceproject(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)
class Civilproject(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)  
class Mechproject(models.Model):  
    Name = models.CharField(max_length=50,default='',null=False)  
    
    Email = models.EmailField(max_length=50,default='',null=False)  
    Project = models.CharField(max_length=50,default='',null=False)  
    Abstract = models.TextField(max_length=1000,default='',null=False)       
