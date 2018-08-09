from __future__ import unicode_literals

from django.db import models

# 前端用户的数据模型

class UserModel(models.Model):
    username = models.CharField(primary_key=True,max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)