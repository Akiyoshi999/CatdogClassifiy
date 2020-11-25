from os import name
from catdog.views import predict, true_result, false_result 
from django.urls import path

from . import views

app_name = 'catdog'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('true/', views.true_result, name='true'),
    path('false/', views.false_result, name='false'),
]