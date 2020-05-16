# 必须！定义一个路由样式列表：名字必须！叫urlpatterns，否则报错
from django.urls import path, re_path

from . import views

urlpatterns = [
    #使用路由匹配请求地址，每匹配成功一个就执行对应的函数视图逻辑
    # path('网络地址正则表达式', '视图函数名')
    # 这个正则表达式Django已经给封装了，我们只要提供一部分

    # 用户注册：http://127.0.0.1:8000/users/register/
    # path('users/register/', views.register),
    path('users/login_test/', views.login_test),
    path('users/print_requestion/', views.print_requestion),

    # 用户注册类视图：# 用户注册：http://127.0.0.1:8000/users/register/
    # 注意：在给类视图注册子路由时需要把类视图转成函数视图
    # 语法：path('网络地址正则表达式', views.类视图.as_view()) !!注意这里有括号
    path('users/register/', views.RegisterView.as_view()),

    # 用户登陆类视图 + re_path 匹配http://127.0.0.1:8000/users/login/
    # re_path里没有封装正则表达式的固定的原则，所以要自己搞
    re_path(r'^users/login/$', views.LoginView.as_view()),


]