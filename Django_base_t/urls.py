"""Django_base_t URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

# 工程的总路由样式列表
urlpatterns = [
    # 默认的后台管理系统的总路由
    path('admin/', admin.site.urls),

    #将users子应用中的子路由注册给总路由
    # path('网络地址前缀/', include('子应用.urls')),
    path('', include('users.urls')), # 每个子应用的子路由只需要注册一次即可
    # 起别名，一般是子应用名字
    path('', include(('request_response.urls', 'request_response'), namespace='request_response')),

    # 图书英雄管理
    path('', include('booktest.urls'))
]
