from django.db import models


# models使用ORM模式和数据库交互，不直接操作数据库
# Create your models here.

# 一个类对应一个表
class Book(models.Model):
    # Book有两个属性id name
    name = models.CharField(max_length=10)  # 书名字段

    # 重写str方法以显示书籍名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)  # 人物名字
    gender = models.BooleanField() # 人物性别

    # 外链的表
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    # 重写人物方法
    def __str__(self):
        return self.name