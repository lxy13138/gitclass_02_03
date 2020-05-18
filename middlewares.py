# 自定义中间件
"""
1。他是标准的python类
2。继承自MiddlewareMixin
3。可以定义中间件方法中的一个或者多个，中间件方法名字不能瞎写
"""

# 导入中间件的抽象的父类
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    """自定义中间件"""

    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1 被调用')
        return response