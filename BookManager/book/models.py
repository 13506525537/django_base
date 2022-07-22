from django.db import models


# Create your models here.

# 一个类对应一个表
# 表名默认为：子应用名_类名  都是小写
class BookInfo(models.Model):
    # id 默认
    # 属性等于字段
    name = models.CharField(max_length=32, unique=True)  # 书名
    pub_date = models.DateField(null=True)  # 出版日期
    readcount = models.IntegerField()  # 阅读数
    commentcount = models.IntegerField(max_length=10)  # 评论数
    is_delete = models.BooleanField(default=False)  # 是否删除

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字


class PersonInfo(models.Model):
    # id 默认
    # 创建字段
    name = models.CharField(max_length=32)
    gender = models.IntegerField()
