from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.


class Users(models.Model):
    # user info
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, primary_key=True)
    password = models.TextField(default='')
    token = models.TextField(default='')

    @classmethod
    def create(cls, user_data):
        user = cls(user_name=user_data['user_name'], email=user_data['email'], password=make_password(user_data['password']))
        return user

    def __str__(self):
        return self.user_name + self.email


class Messages(models.Model):
    # rsp send message to mobile
    email = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    message = models.TextField()
    # message is posted to mobile or not
    active = models.BooleanField(default=True)
    time = models.DateTimeField()

    @classmethod
    def create(cls, data):
        # do something with the book
        message = cls(email=data['email'], type=data['type'], message=data['message'], time=data['time'])
        return message

    # def __init__(self, data):
    #     super.__init__(data)
    #     self.email = data['email']
    #     self.type = data['type']
    #     self.message = data['message']
    #     self.time = data['time']
    #     self.active = True

    # def __str__(self):
    #     return str(self.email) + '---' + self.type + '---' + self.message + '---' + str(self.time) + '---' + \
    #            str(self.active)

