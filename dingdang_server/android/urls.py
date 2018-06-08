from django.urls import path
from . import views

app_name = 'android'

urlpatterns = [
    path('register/', views.register, name='resister'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:email>/get_messages/', views.get_messages, name='get_messages'),
]