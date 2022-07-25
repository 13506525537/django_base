import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

from book.models import BookInfo


def index(request):
    return render(request, 'index.html')


def create_book(request,):
    # # 新增一本书籍
    # book = BookInfo.objects.create(
    #     name = '雪山飞狐',
    #     pub_date = '2020-10-1'
    # )
    # book.save()
    return HttpResponse('小镇做题家')


# 查询字符串
# 以？为分割，前面为请求路径，后面为查询参数，多数据采用&连接

def shop(request, city_id, shop_id):
    query_params = request.GET  # 获取get中的参数,以QueryDict形式返回，还具有一键多值的特性
    print(query_params)
    # 使用getlist获取一键多值的值
    order = query_params.getlist('keyword')
    print(order)
    return HttpResponse(f'{city_id}的{shop_id}存在！')

def class_no(request,class_no):
    query_params = request.GET # 获取name的参数
    name = query_params.get('name')

    return HttpResponse(f'你好，我是{class_no}班的{name}')

def register(request):
    body_str = request.body.decode() # 获取body后解码，得到字符串
    body = json.loads(body_str) # 用json.loads转成字典
    print(body)
    # print(type(body))
    # print(request.META)# 获取请求头
    print(request.META['SERVER_PORT'])

    return render(request,template_name='register.html')
    # return HttpResponse('ok')

def response(request): # 测试响应
    response = HttpResponse('res',status=200) # 第一个参数为响应体，第二个为状态码
    response['name']='itcast' #可以通过这种方式这只响应头
    return response
    # 1XX 消息
    # 2XX 成功
    # 3XX 重定向
    # 4XX 客户端 404路由有问题
    # 5XX 服务器