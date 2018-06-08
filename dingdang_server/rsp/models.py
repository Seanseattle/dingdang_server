from django.db import models

# Create your models here.


class Users(models.Model):
    # user info
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models


class Messages(models.Model):
    # rsp send message to mobile
    email = models.ForeignKey(on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    message = models.TextField()
    time = models.TimeField()

