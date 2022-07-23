from django.shortcuts import render

# Create your views here.

# 定义首页
from django.http import HttpRequest
from django.http import HttpResponse


# 首页
def index(request):
    # 在这里实现增删改查
    return HttpResponse("ok")


# 导入数据库对象，可以用shell快速验证查询结果
from book.models import BookInfo
from book.models import PersonInfo

"""
################增加代码####################
# 方式1
book = BookInfo(
    name='西厢记',
    pub_date='2000-1-1',
    readcount=10,
    commentcount=14,
)
# 必须要调用save方法才能将对象保存到数据库
book.save()

# 方式2
# objects -- 相当于一个代理  实现增删改查
#
BookInfo.objects.create(
    name='笑傲江湖',
    pub_date='2020-1-1',
    readcount=19,
    commentcount=84,
)

################修改数据###############

# 方式1
# select * from bookinfo where id = 4;
book = BookInfo.objects.get(id=4)
book.name = '新白娘子传奇' # 修改名字
book.save()

# 方式2 # update()一定要用filter(),  get()只能查询用
BookInfo.objects.filter(id=4).update(name='红楼梦',commentcount=6)
"""

"""
###############删除数据#############
# 方式1
book = BookInfo.objects.get(id=6)
# 删除分两种，一种标记删除，一种物理删除
book.delete()

# 方式2 get和filter(过滤)都可以
BookInfo.objects.get(id=5).delete()
BookInfo.objects.filter(id=5).delete()
"""

"""
##################查询方式###########
# get()查询单一结果，如不存在返回DoesNotExits
try:
    BookInfo.objects.get(id=4)
except Exception as e:
    print(e)
    print("查询结果不存在")
# all()查询多个结果，以列表形式返回
BookInfo.objects.all()
# count查询结果数 两种方式都可以，推荐第一种
BookInfo.objects.all().count()
BookInfo.objects.count()

###############过滤查询#############
# 实现where的功能
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 语法
# filter(属性名__运算符=值)  获取n个结果 n=0,1,2...
# exclude(属性名__运算符=值) 获取n个结果 n=0,1,2...
# get(属性名__运算符=值)   获取1个结果 或者异常

# 查询编号为1的图书
book=BookInfo.objects.get(id=1)
book=BookInfo.objects.get(id__exact=1)
book=BookInfo.objects.get(pk=1)

# 查询名字包含浒的书
BookInfo.objects.filter(name__contains='浒')
# 查询书名以记结尾的图书
BookInfo.objects.filter(name__endswith='记')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询id为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书 大于gt 大于等于gte 小于lt 小于等于lte
BookInfo.objects.filter(id__gt=2)
BookInfo.objects.filter(id__lte=2)
# 查询id不等于3的图书
BookInfo.objects.exclude(id__exact=1)
# 查询2022年发布的图书
BookInfo.objects.filter(pub_date__year=2022)
# 查询2020年6月后发布的图书
BookInfo.objects.filter(pub_date__gt='2022-6-30')
"""

"""
###############两个属性的比较：F对象##########
from django.db.models import F

# 查询阅读量大于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))
# 查询阅读量大于评论量2倍的图书
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)


#################Q对象##############

# 并且查询
# 查询阅读量小于3，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=3).filter(id__lt=3)
BookInfo.objects.filter(readcount__gt=3,id__lt=3)

# 或者查询
from django.db.models import Q
# 或者语法 模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性值__运算符=值)|...)
# 查询阅读数大于7或者id小于3的图书
BookInfo.objects.filter(Q(readcount__gt=7)|Q(id__lt=3))

# not查询
# id不等于3的图书
BookInfo.objects.filter(~Q(id=3))
"""

########################聚合函数###############

# Sum,Max,Min,Avg,Count
from django.db.models import Sum,Max,Min,Avg,Count
from django.db.models import Q
BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.filter(Q(name__contains='水')|Q(name__contains='梦')).aggregate(Sum('readcount')
)

#######################升序降序#######
BookInfo.objects.all().order_by('readcount') # 升序
BookInfo.objects.all().order_by('-readcount') # 降序

######################关联查询############################################
# 两个表级联操作

# 查询书籍为1的所有人物信息
book_info = BookInfo.objects.get(id=1)
# 一对多的关联模型中系统会为我们自动天机一个关联模型小写_set的字段
# personinfo_set=[PersonInfo,PersonInfo,....]
book_info.personinfo_set.all()

# 查询诸葛亮是哪本书的
person = PersonInfo.objects.get(name='诸葛亮')
person.book.name # person.book是个对象，用对象.属性调用属性

##################关联查询的过滤查询######################
# 语法形式
# 查询1的数据，条件为n
# 模型类名.objects.filter(关联类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为“林黛玉”
BookInfo.objects.filter(personinfo__name__exact='林黛玉')
# 查询图书，要求图书中人物的描述包含‘武力型’
book_list = BookInfo.objects.filter(personinfo__description__contains='武')

# 查询图书阅读量大于30的所有人物
PersonInfo.objects.filter(book__readcount__gt=30)