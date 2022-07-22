# APP 路由
from django.urls import path
from book.views import index

urlpatterns = [path('index/', index),
               ]
