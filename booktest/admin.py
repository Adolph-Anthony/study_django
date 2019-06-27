from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    '''样式调整,需要注册,不用添加装饰器'''
    list_display = ['id','btitle','pub_date']

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    '''样式调整'''
    #每页显示五个英雄
    list_per_page = 5
    #顶部底部显示的属性，设置为True在顶部显示，设置为False不在顶部显示，默认为True。
    actions_on_top = True
    actions_on_bottom = True
    #将数据库中的表字段取出作为列
    list_display = ['id','hname','hgender','hcomment','hbook']
    #增加过滤器功能
    list_filter = ['hbook','hgender']
    #增加字段搜索框
    search_fields = ['hname']

#注册管理模型类
admin.site.register(BookInfo,BookInfoAdmin)
# admin.site.register(HeroInfo)