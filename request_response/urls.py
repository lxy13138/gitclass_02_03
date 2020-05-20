from django.urls import path, re_path
from . import views

# 在总路由中，注册自定义路由转换器
# 导包
from django.urls import register_converter
from converters import MobileConverter


# 调用注册路由转换器的方法，完成路由转换器的注册
# register_converter(自定义的路由转换器类, '别名')
register_converter(MobileConverter, 'mobile')

urlpatterns = [
    # 测试提取查询字符串：GET http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('request_response/querystring/', views.QSParamView.as_view()),
    # 测试提取表单类型请求体参数 POST：http://127.0.0.1:8000/formdata/
    path('formdata/', views.FormDataParamView.as_view()),
    # 测试提取非表单类型请求体参数：http://127.0.0.1:8000/json/
    path('json/', views.JSONParamView.as_view()),
    # 测试path()提取普通路径参数：http://127.0.0.1:8000/url_param1/18/
    # 提取路径参数是在路由系统里面完成的，因为路径是在路由系统进行处理
    # path('url_param1/18/', views.URLParam1View.as_view()),
    # 路由中提取路径参数时，使用的关键字，必须跟视图中参数名一致(age)
    # path('url_param1/<路由转换器，提取路径参数:变量接收提取的路径参数>/', views.URLParam1View.as_view()),
    path('url_param1/<int:age>/', views.URLParam1View.as_view()),

    # 测试path()中自定义路由转换器提取路径参数：手机号 http://127.0.0.1:8000/url_param2/18500001111/
    path('url_param2/<mobile:phone_num>/', views.URLParam2View.as_view()),

    # 测试re_path提取路径参数http://127.0.0.1:8000/url_param3/18500001111/
    re_path(r'^url_param3/(?P<phone_num>1[3-9]\d{9})/$', views.URLParam3View.as_view()),

    # 测试HttpResponse：http://127.0.0.1:8000/response1/
    path('response1/', views.Response1View.as_view()),

    # 测试JSONResponse：http://127.0.0.1:8000/json_resp/
    path('json_resp/', views.JSONResponseView.as_view()),

    # 测试重定向:首页视图:http://127.0.0.1:8000/index/
    path('index/', views.IndexView.as_view(), name='index'),
    # 测试重定向:登陆视图:http://127.0.0.1:8000/login_redirect/
    path('login_redirect/', views.LoginRedirectView.as_view()),
]