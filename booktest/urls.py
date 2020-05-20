# 必须！定义一个路由样式列表：名字必须！叫urlpatterns，否则报错
from django.urls import path, re_path

from . import views

urlpatterns = [
    #使用路由匹配请求地址，每匹配成功一个就执行对应的函数视图逻辑
    # path('网络地址正则表达式', '视图函数名')
    # 这个正则表达式Django已经给封装了，我们只要提供一部分

    # http://127.0.0.1:8000/data1
    path('booktest/data1/', views.TestModelVoew1.as_view()),


]