"""
中间件页面
要在setting页面设置
"""
# 定义中间件
# 1. 导入中间件
from django.utils.deprecation import MiddlewareMixin


# 2.创建相关类
class MiddlewareTest(MiddlewareMixin):

    def process_request(self, request):
        print('每次请求前都会调用')
        username = request.COOKIES.get('username')
        if username is None:
            print('没有用户信息')
        else:
            print('有用户信息')

    def process_response(self, request, response):
        print('每次响应前都会调用')
        return response
