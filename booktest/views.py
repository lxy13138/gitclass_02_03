from django.shortcuts import render
from django.views import View
from django import http

from booktest.models import BookInfo
# Create your views here.

class TestModelVoew1(View):
    """测试增改删
    GET http://127.0.0.1:8000/data1
    """

    def get(self, request):

        # 修改：save（）、update
        ##########update方法################
        # 语法：模型类.objects.filter(id=6).update(模型类属性=新值)
        BookInfo.objects.filter(id=6).update(btitle='三国志')


        ##########save方法################
        # 查询出要修改的记录/模型对象            是将操作完的数据同步到数据库，所以新增和修改都可以用save
        # book = BookInfo.objects.get(id=5)
        #
        # # 新值覆盖旧值
        # book.btitle = '西游记后传'
        #
        # # 同步新值
        # book.save()




        # 新增：save（）、create（）
        ##########create方法################
        # 语法：模型类.模型管理器.create(模型属性=值)
        # 模型管理器：是由Django提供并封装的一个对象（objects），用于调用ORM的接口方法，固定的语法
        # BookInfo.objects.create(
        #     btitle='三国演义',
        #     bpub_date='2020-5-21',
        #     bread=100,
        #     bcomment=200,
        # )

        ##########save方法################
        # # save()方法                 是将操作完的数据同步到数据库，所以新增和修改都可以用save
        # # 使用模型类初始化模型对象
        # book = BookInfo()
        #
        # # 给模型对象的属性赋值
        # book.btitle = '西游记'
        # book.bpub_date = '2020-5-20'
        # book.bread = 20
        # book.bcomment = 30
        # # is_delete不要赋值，有默认值
        # # book.is_delete =
        #
        # # 使用模型对象调用save()
        # # save():它是将模型对象属性中的值同步到对应的数据表字段中
        # book.save()

        return http.HttpResponse('测试增改删')
