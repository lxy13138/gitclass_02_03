from django.db import models

# Create your models here.

"""
定义模型属性，映射数据表字段
字段有哪些，属性就有哪些，其中id主键默认不需要处理
字段类型是什么，定义的时候就设置什么

"""

class BookInfo(models.Model):
    """图书信息：演示一对多，一方"""
    # 定义模型属性，映射数据表字段
    btitle = models.CharField(max_length=64, verbose_name='书名')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除') # 逻辑删除，设计一个bool类型，可以设置标记假设删除

    class Meta:
        """模型类的元类：用于修改、配置模型类对应的数据表"""
        db_table = 'tb_bookinfo'  # 自定义数据库表名


class HeroInfo(models.Model):
    """英雄信息：演示一对多，多方"""
    # 确定性别字段的取值范围
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    # 看这个外键是这么设置的
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='英雄属于的图书')
    hname = models.CharField(max_length=20, verbose_name='人名')
    # 看这个性别的选择，上面设置了范围，类型是元组嵌套元组，这里设置choices=设置的范围，
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'

    def __str__(self):
        return self.hname
