from django.shortcuts import render

# Create your views here.
"""
视图
所谓试图 其实就是python函数
试图函数有两个要求：
    1. 视图函数的第一个参数就是接受请求
    2. 必须返回一个响应
"""
from django.http import HttpResponse
from django.http import HttpRequest

# 定义好后期望用户输入/index/访问函数
def index(request):

    return HttpResponse("ok")