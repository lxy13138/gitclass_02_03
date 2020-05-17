from django.shortcuts import render
from django.views import View
from django import http
import json

# Create your views here.

class JSONParamView(View):
    """测试提取非表单类型请求体参数
       POST http://127.0.0.1:8000/json/
       JSON中传递username，password
    """
    def post(self, request):
        """提取JSON中的username、password"""
        # 先获取原始的非表单类型的请求体数据，无论是什么，都是使用request.body
        origin_data = request.body

        # 根据具体的非表单类型的请求体数据的类型，去完成数据的解析：JSON为例
        # 如何解析原始JSON数据
        # load作用：将原始json数据转成字典
        json_dict = json.loads(origin_data)

        # 最后从参数字典中取出需要的数据
        username = json_dict.get('username')
        password = json_dict.get('password')
        print(username, password)

        return http.HttpResponse('非表单类型请求体参数: JSON')



class FormDataParamView(View):
    """测试提取表单类型请求体参数
    POST：http://127.0.0.1:8000/formdata/
    请求体中传递username/password
    """

    def post(self, request):
        """
        从请求体中接收username、password
        :param request:
        :return:
        """
        # form_data = request.POST
        # username = form_data.get('username')
        # password = form_data.get('password')

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        return http.HttpResponse('测试提取表单类型的请求体数据')



class QSParamView(View):

    def get(self, request):
        """
        从请求对象中提取查询字符串参数name，age
        request.GET:专门用于提取请求地址中的查询字符串参数的
        :param request:请求对象
        :return:响应对象
        """
        # query_str_param = request.GET
        # name = query_str_param.get('name')
        # 注意点：提取查询字符串参数不区分请求方式，即使客户端进行POST方式的请求，
        #        依然可以通过request.GET获取请求中的查询字符串参数。
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name,age)

        return http.HttpResponse('测试提取查询字符串')