from django.shortcuts import render
#导入构造响应对象的模块
from django import http
#导入类视图
from django.views import View

# Create your views here.

#############演示path,re_path################

class LoginView(View):
    """用户登陆类视图
    http://127.0.0.1:8000/users/login/
    """

    def get(self, request):
        return http.HttpResponse('假装这是个用户登陆页面')

#############定义类视图################

class RegisterView(View):
    """
    用户注册类视图
    GET，POST：http://127.0.0.1:8000/users/register/
    注意点：我们定义了哪些跟请求方法同名的函数，那么该视图只能接收对应的请求方法
    """
    #方法名要和请求方法同名
    def get(self, request):
        """
        处理GET逻辑
        :param request: 请求对象
        :return: 响应对象
        """
        return http.HttpResponse('这里假装返回注册页面')
    def post(self, request):
        """
        处理POST逻辑
        :param request:请求对象
        :return: 响应对象
        """
        return http.HttpResponse('这里假装实现注册逻辑')





#############定义函数视图################

def register(request):
    """
    用户注册函数视图
    只有该函数被调用才会被执行
    http://127.0.0.1:8000/users/register/
    :param request: 请求对象，是Django封装好的
    :return: 响应对象
    """
    return http.HttpResponse('假装这是个注册页面')

def login_test(request):
    return http.HttpResponse('演习演习演习')

def print_requestion(request):
    # print('返回的数据：', request)
    return http.HttpResponse('返回给我看看')


# def register(请求对象):
#     # 用户注册函数视图
#     return 响应对象

# 工程文件执行流程（返回http://127.0.0.1:8000/users/register/）：
# 1、请求发出之后由工程总路由接收到，在总路由列表自上而下遍历匹配项（而且django会自动只匹配8000/后的部分，识别出是users下的路由）
#    匹配到已经在总路由注册过的users.urls，也就是include函数内部的参数，就会进入到users里的url
# 2、进入users的url里后会再拿users后的register/进一步匹配路由，匹配成功就调用path('users/register/', views.register)里的
#    views.register这个函数，由此进入到user的view里执行函数register()