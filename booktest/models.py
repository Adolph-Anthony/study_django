from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    '''创建自定义管理器'''
    def all(self):
        return self.filter(is_delete = False)




#定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    #创建新字段存储图片保存路径
    logo = models.ImageField(upload_to='booktest', verbose_name='主图片', null=True)
    # 默认表名
    # booktest_bookinfo
    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle
    #补充自定义管理器对象,模型类将不会再存在objects
    # query = BookInfoManager()
    def pub_date(self):
        #调整返回样式,从日期转化成字符串
        return self.bpub_date.strftime('%Y年%m月%d日')
    #给pub_date函数补充属性,将页面展示的字段名字改成 发行日期
    pub_date.short_description = '发行日期'
    #自定义的字段没有排序功能,增加字段排序功能
    pub_date.admin_order_field = 'bpub_date'


#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')

    # 来指明choices这个字段可选范围,传入元组数据,要么就是0要么就是1,后面跟的字符方便理解 代表 0 是代表什么意思等
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')

    # 外键只需要指明 hbook 跟哪个 模型类(BookInfo) 形成外键就可以了
    # on_delete 代表被关联的数据被删除如何处理  CASCADE:级联
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname