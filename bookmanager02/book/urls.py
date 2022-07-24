"""
app 路由表
"""
from book.views import index, create_book, shop, class_no,register
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('create/', create_book),  # 获取请求中路径的参数*****
    path('shop/<city_id>/<shop_id>', shop),  # 获取请求中路径的参数*****
    path('school/<class_no>', class_no),
    path('register/', register)
]
