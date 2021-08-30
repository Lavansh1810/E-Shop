from django.db import models
from datetime import datetime

class Kitchen(models.Model):
    product_id = models.AutoField
    is_published = models.BooleanField(default=False)
    is_hot= models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=100,default="",)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="")
    desc=models.TextField(max_length=2000,default="")
    def __str__(self):
        return '%s' % (self.name)

class Clothing(models.Model):
    product_id = models.AutoField
    is_published = models.BooleanField(default=False)
    is_hot= models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=100,default="",)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="")
    desc=models.TextField(max_length=2000,default="")
    def __str__(self):
        return '%s' % (self.name)

class Shoes(models.Model):
    product_id = models.AutoField
    is_published = models.BooleanField(default=False)
    is_hot= models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=100,default="",)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="")
    desc=models.TextField(max_length=2000,default="")
    def __str__(self):
        return '%s' % (self.name)

class Electronics(models.Model):
    product_id = models.AutoField
    is_published = models.BooleanField(default=False)
    is_hot= models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=100,default="",)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="")
    desc=models.TextField(max_length=2000,default="")
    def __str__(self):
        return '%s' % (self.name)

class Gym(models.Model):
    product_id = models.AutoField
    is_published = models.BooleanField(default=False)
    is_hot= models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=100,default="",)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="")
    desc=models.TextField(max_length=2000,default="")
    def __str__(self):
        return '%s' % (self.name)

class Daliy_Use(models.Model):
    product_id = models.AutoField
    is_published = models.BooleanField(default=False)
    is_hot= models.BooleanField(default=False)
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=100,default="",)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="")
    desc=models.TextField(max_length=2000,default="")
    def __str__(self):
        return '%s' % (self.name)
