from django.urls import path
from . import views
'''rsp upload data to servers'''

app_name = 'rsp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
]