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
    username = res.get('username')
    password = res.get('password')
    # 2. 服务器设置cookie信息
    response = HttpResponse('set_cookie')
    response.set_cookie('username', username, max_age=30)
    # max_age是一个秒数，不设置的话默认为浏览器关闭cookies过期
    # 删除cookie
    # request.delete_cookie('name')
    response.set_cookie('password', password, max_age=30)
    return response


def get_cookies(request):
    # 获取cookie
    print(request.COOKIES)
    # request.COOKIES是字典数据
    name = request.COOKIES.get('username')
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
    try:
        request.session['user_id'] = user_id
        request.session['username'] = username
    except Exception as e:
        print(e)
        print('ERROR: session设置失败')
    return HttpResponse('set_session')


def get_session(request):
    # user_id = request.session['user_id']
    # username = request.session['username']
    # 如果没有session的话以上方法会报异常，可以用get去避免异常，get如果没有查询到返回None
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    # session的有效期
    # 如果value是个整数，session将在value秒后结束
    # 如果value是个0，session将在浏览器关闭时过期
    # 如果value为None，那么session将采用系统默认值，默认为两周，可以通过setting中的
    # SESSION_COOKIE_AGE来设置全局默认值
    request.session.set_expiry(60)

    content = '{},{}'.format(user_id, username)
    return HttpResponse(content)


#########################session保存到redis######################
# 在setting中设置
# session删除
# request.session.clear() 清除所有session的数值,在储存中保留key和value中删除值的部分
# request.session.flush() 清除session中的数据，保留key，在储存中删除整条数据
# del request.session['键'] 删除session中指定键及值，在储存中只删除某个键及对应的值


##################################类视图#############################
# 常规在函数中定义
def login(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('get 逻辑')
    else:
        return HttpResponse('post 逻辑')


# 类视图定义
"""
类视图的定义
class 类视图名字(View):
    def get(self,request):
        return HttpResponse('XXX')
        
    def http_method_lower(self,request):
        return HttpResponse('XXX')

"""
# 1.继承自View，url路径中必须要加视图函数名
from django.views import View


# 2.定义类,使用小写的get,post来进行区分请求方式
class LoginView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 1.获取
        userinfo = request.POST
        username = userinfo.get('username')
        password = userinfo.get('password')

        request.session['username'] = username
        request.session['password'] = password

        request.session.set_expiry(60)

        return redirect('/overview/')


##############个人中心页面###########
"""
我的订单、个人中心页面
如果登录用户    可以访问
如果未登录用户   不可以访问跳转到登陆页面
"""


# 第一种  使用装饰器进行判断是否登录
class OrderView(View):

    @staticmethod
    def is_login(func):
        def innerfunc(self, request):
            is_login = False
            if request.session.get('username') == 'admin' and request.session.get('password') == '123456':
                is_login = True

            if is_login:
                return func(self, request)
            else:
                return redirect('/login/')

        return innerfunc

    @is_login
    def get(self, request):
        return render(request, 'index.html')


# 第二种  使用django自带的判断是否登录的类来进行判断
from django.contrib.auth.mixins import LoginRequiredMixin

# 判断是否登录，没有登录跳转登录页
# LoginRequiredMixin 必须放在View前
# LoginRequiredMixin内部会以用户是否登录admin站点，如果未登录，
#  跳转accounts/login/路径上
class IsLogin(LoginRequiredMixin, View):

    def get(self, request):
        return HttpResponse('ok get')

    def post(self, request):
        return HttpResponse('ok post')

# 第三种  使用中间件进行判断