"""server URL Configuration

The `urlpatterns` list routes URLs to action. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function action
    1. Add an import:  from my_app import action
    2. Add a URL to urlpatterns:  path('', action.home, name='home')
Class-based action
    1. Add an import:  from other_app.action import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jsapp.action import IndexController,LoginController,KgController,MapController
urlpatterns = [
    #登录模块
    path('login/', LoginController.login),
    #主界面模块
    path('index/', IndexController.index),
    #图谱模块
    path('entitykg/', KgController.entitykg),#实体图谱
    path('orderkg/', KgController.orderkg),#指令推理
    #地图模块
    path('map/', MapController.map),
]
