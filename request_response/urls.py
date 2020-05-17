from django.urls import path
from . import views

urlpatterns = [
    # 测试提取查询字符串：GET http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/', views.QSParamView.as_view()),
    # 测试提取表单类型请求体参数 POST：http://127.0.0.1:8000/formdata/
    path('formdata/', views.FormDataParamView.as_view()),
    # 测试提取非表单类型请求体参数：http://127.0.0.1:8000/json/
    path('json/', views.JSONParamView.as_view()),
]