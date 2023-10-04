"""
URL configuration for dgame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from dgame.views import *
admin.autodiscover()

# 注册路径 html 转后端python
urlpatterns = [
    re_path(r'^$', index, kwargs=None, name = 'index'),
	re_path(r'^(\d+)/$', ajax, kwargs=None, name='ajax'),
	re_path(r'^search/(\w+)/$', search, kwargs=None, name = 'search'),
	re_path(r'^searchtype/(\w+)/$', searchtype, kwargs=None, name = 'searchtype'),
	re_path(r'^searchPlayers/(\w+)/(\w+)/(\w+)/(\w+)/$', searchPlayers2, kwargs=None, name = 'searchPlayers'),
	re_path(r'^getinfo/(\w+)/$', ajaxGetInfo, kwargs=None, name='ajaxGetInfo'),
	re_path(r'^searchplayerinfo/$', searchPlayerInfo, kwargs=None, name='searchPalyerInfo'),
	re_path(r'^searchbaninfo/(\w+)/(\w+)/(\w+)/(\w+)/$', searchBanInfo, kwargs=None, name='searchBanInfo'),
	re_path(r'^sendMail/$', sendMail, kwargs=None, name='sendMail'),
	re_path(r'^banPlayer/$', banPlayer, kwargs=None, name='banPlayer'),
	re_path(r'^setGmPrivilege/(\w+)/(\w+)/(\w+)/$', setGmPrivilege, kwargs=None, name='setGmPrivilege'),
	re_path(r'^searchgminfo/(\w+)/(\w+)/(\w+)/(\w+)/$', searchGmInfo, kwargs=None, name='searchGmInfo'),
	re_path(r'^sendAllMail/$', sendAllMail, kwargs=None, name='sendAllMail'),
	re_path(r'^notice/$', notice, kwargs=None, name='notice'),
	re_path(r'^saveRTF/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/$', saveRTF, kwargs=None, name='saveRTF'),
]
