from django.db import models

# Create your models here.
"""
模型类需要继承models.Model
"""


# 一个类对应一个表
# 表名默认为：子应用名_类名  都是小写
class BookInfo(models.Model):
    # id 默认
    # 属性等于字段
    name = models.CharField(max_length=32, unique=True, )  # 书名
    pub_date = models.DateField(null=True)  # 出版日期
    readcount = models.IntegerField()  # 阅读数
    commentcount = models.IntegerField()  # 评论数
    is_delete = models.BooleanField(default=False)  # 是否删除

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字


class PersonInfo(models.Model):
    # id 默认

    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    # 创建字段
    name = models.CharField(max_length=32, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)  # 枚举类型
    description = models.CharField(max_length=32)
    is_delete = models.BooleanField(default=False)

    # 系统会自动为外键添加 _id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, default="")
    # on_delete可选常量：
    # 1. SET_NULL 设为Null
    # 2. PROTECT 不让删除并抛出异常
    # 3. CASCADE 级联操作，一起删了
    # 4. SET() 设为某个值

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'personinfo'  # 修改表的名字
