from django.shortcuts import render

# Create your views here.

# 定义首页
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    return HttpResponse("ok")