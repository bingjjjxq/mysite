# -*- coding:utf-8 -*-
__author__ = 'Journey'
__time__ = '2019/3/25 15:35'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]

