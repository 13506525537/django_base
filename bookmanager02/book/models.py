from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改表名

    def __str__(self): # 返回对象名
        return self.name


class PeopleInfo(models.Model):
    CHOICE = (
        (0, "male"),
        (1, "female")
    )  # choice用元组

    name = models.CharField(max_length=10, unique=True)
    gender = models.IntegerField(choices=CHOICE)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = 'peopleinfo'  # 修改表名

    def __str__(self): # 返回对象名
        return self.name
