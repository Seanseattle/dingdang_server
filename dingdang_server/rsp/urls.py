from django.urls import path
from . import views
'''rsp upload data to servers'''

app_name = 'rsp'

urlpatterns = [
    path('login/', views.LoginView name='login'),
    path('upload/', name='upload'),
]