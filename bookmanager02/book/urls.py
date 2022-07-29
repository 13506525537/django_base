"""
app 路由表
"""
from book.views import IsLogin,OrderView, LoginView, login, get_session, set_session, get_cookies, set_cookies, index, redict, \
    create_book, shop, \
    class_no, register, response, jsonres
from django.urls import path

from django.urls import converters  # 转化器模块，里面可以自己添加

urlpatterns = [
    path('index/', index),
    path('create/', create_book),  # 获取请求中路径的参数*****
    path('shop/<int:city_id>/<int:shop_id>', shop),  # <转化器名称:变量名> 转换器会对变量进行正则验证
    path('school/<class_no>', class_no),
    path('register/', register),
    path('res/', response),
    path('jsonres/', jsonres),
    path('redict/', redict),
    path('setcookies/', set_cookies),
    path('getcookies/', get_cookies),
    path('setsession/', set_session),
    path('getsession/', get_session),
    path('login/', LoginView.as_view()),  # 这里要写试图函数的名字
    path('overview/', OrderView.as_view()),
    path('islogin/',IsLogin.as_view()),
]
