import json

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpRequest

from book.models import BookInfo


def index(request):
    return render(request, 'index.html')


def create_book(request, ):
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


def class_no(request, class_no):
    query_params = request.GET  # 获取name的参数
    name = query_params.get('name')

    return HttpResponse(f'你好，我是{class_no}班的{name}')


def register(request):
    body_str = request.body.decode()  # 获取body后解码，得到字符串
    body = json.loads(body_str)  # 用json.loads转成字典
    print(body)
    # print(type(body))
    # print(request.META)# 获取请求头
    print(request.META['SERVER_PORT'])

    return render(request, template_name='register.html')
    # return HttpResponse('ok')


def response(request):  # 测试响应
    response = HttpResponse('res', status=200)  # 第一个参数为响应体，第二个为状态码
    response['name'] = 'itcast'  # 可以通过这种方式这只响应头
    return response
    # 1XX 消息
    # 2XX 成功
    # 3XX 重定向
    # 4XX 客户端 404路由有问题
    # 5XX 服务器


from django.http import JsonResponse


def jsonres(request):
    # info = {
    #     'name' : '小李',
    #     'address': '上海'
    # }
    girl_friends = [
        {
            'name': '小李',
            'address': '上海'
        },
        {
            'name': 'rose',
            'address': '浙江'
        }
    ]
    return JsonResponse(girl_friends, safe=False)
    # safe 为安全锁
    # safe = True 表示是字典数据
    # safe = False 表示可以传输非字典数据


def redict(request):  # 重定向

    return redirect('http://www.baidu.com')


# 第二次请求之后访问地址会携带cookie信息，来判断用户身份

def set_cookies(request):
    # 1. 获取查询字符串数据
    res = request.GET
    username = res['username']
    password = res['password']
    # 2. 服务器设置cookie信息
    response = HttpResponse('set_cookie')
    response.set_cookie('name', username, max_age=30)
    # max_age是一个秒数，不设置的话默认为浏览器关闭cookies过期
    # 删除cookie
    # request.delete_cookie('name')
    response.set_cookie('password', password, max_age=30)
    return response


def get_cookies(request):
    # 获取cookie
    print(request.COOKIES)
    # request.COOKIES是字典数据
    name = request.COOKIES.get('name')
    return HttpResponse(name)


####################session############
'''
1. session 保存在服务器端
2. session 依赖于cookie
'''


# 第一次请求在 服务器端设置session信息
# 服务器同时生成一个sessionid的cookie信息
# 浏览器收到信息后会保存好 cookie

# 第二次请求时会携带sessionid，服务器会严重，没问题后会读取相关数据

def set_session(request):
    # 1. 模拟获取用户的信息
    username = request.GET.get('username')
    # 2. 设置session信息
    # 假如我们通过模型查询到了用户的信息,session是以字典形式保存信息
    # 在实现session时顺便实现了cookie
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse('set_session')


def get_session(request):
    # user_id = request.session['user_id']
    # username = request.session['username']
    # 如果没有session的话以上方法会报异常，可以用get去避免异常，get如果没有查询到返回None
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    content = '{},{}'.format(user_id, username)
    return HttpResponse(content)
