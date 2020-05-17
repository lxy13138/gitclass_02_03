from django.shortcuts import render
from django.views import View
from django import http
import json
from django.shortcuts import redirect

# Create your views here.

###########以下代码演示响应###############

class LoginRedirectView(View):
    """测试重定向:登陆页面，成功后自动跳转到首页
    POST http://127.0.0.1:8000/login_redirect/
    """
    def post(self, request):
        # 假装正在处理登录逻辑
        # 假装登录逻辑处理完成
        # ......

        # 将用户通过重定向引导到首页
        # redirect('要跳转到的页面')可以跳，这个函数的第一个参数就是要去的页面
        #注意：！请求发起者对应的地址是/login_redict/,
        #       要重定向的地址：index/，没写根路径
        #       结果：http默认成这样/login_redict/index/，就会出错
        """所以，这里的路径要写根路径：/index/    再不济写全也行：http://127.0.0.1:8000/index/"""
        return redirect('/index/')


class IndexView(View):
    """测试重定向:首页视图
    GET http://127.0.0.1:8000/index/
    """
    def get(self, request):
        return http.HttpResponse('假装这是个网站首页')

class JSONResponseView(View):
    """测试JSONResponse
    http://127.0.0.1:8000/json_resp/
    """
    def get(self, request):
        dict_data = {
            'city':'北京',
            'subject':'python'
        }
        # JsonResponse默认传递字典参数
        # 扩展：JsonResponse默认传递字典，想要传别的类型的参数时要设置safe=False，详情请commot + b查看JsonResponse函数
        return http.JsonResponse(dict_data)


class Response1View(View):
    """测试HttpResponse
    http://127.0.0.1:8000/response1/
    提示：默认HttpResponse响应html字符串
         但是如果我们响应别的数据怎么办？
         比如响应图片数据
            HttpResponse（响应体：图片的原始数据， content_type='image/jpg'）
    """
    def get(self, request):
        """接收请求，处理逻辑，响应结果"""
        #return http.HttpResponse(content='响应体', content_type='文件数据类型：默认text/html', status='状态：默认200')
        # return http.HttpResponse(content='演示HttpResponse', content_type='text/html', status=200)
        # 简写
        # return http.HttpResponse(content='演示HttpResponse')
        # return http.HttpResponse('演示HttpResponse2222222')
        response = http.HttpResponse('演示HttpResponse333333')
        return response


###########以下代码演示请求###############


class URLParam3View(View):
    """
    测试re_path提取路径参数
    http://127.0.0.1:8000/url_param3/18500001111/
    """
    def get(self, request, phone_num):
        """提取路径参数手机号"""
        print(phone_num)
        return http.HttpResponse('测试re_path()提取路径参数：')

# 提取手机号的
class URLParam2View(View):
  """测试path()中自定义路由转换器提取路径参数：手机号
  http://127.0.0.1:8000/url_param2/18500001111/
  """

  def get(self, request, phone_num):
      """
      :param phone_num: 路由提取的关键字参数
      """
      return http.HttpResponse('测试path()提取路径参数手机号：%s' % phone_num)


class URLParam1View(View):
    """测试path()提取普通路径参数
    GET http://127.0.0.1:8000/url_param1/18/
    """
    def get(self, request, age):
        """接收路径参数"""
        print(age)
        return http.HttpResponse('测试path()提取普通路径参数')



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
