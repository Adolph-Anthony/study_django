from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    '''样式调整,需要注册,不用添加装饰器'''
    pass

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    '''样式调整'''
    pass


#注册管理模型类
admin.site.register(BookInfo,BookInfoAdmin)
# admin.site.register(HeroInfo)