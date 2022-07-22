from django.contrib import admin

# Register your models here.
# 从book,models导入
from book.models import Book,PeopleInfo

# 注册模型类
admin.site.register(Book)
admin.site.register(PeopleInfo)
# 重新运行django