from django.db import models

# Create your models here.

# 新建表
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)



class user(models.Model):
    account = models.CharField(max_length=64)
    passwd = models.CharField(max_length=64)
    authority = models.CharField(max_length=64)
    authority.default = "newbie"
    registTime = models.DateTimeField()