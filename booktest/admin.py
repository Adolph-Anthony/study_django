from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, HeroInfo

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    '''样式调整'''
    pass

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    '''样式调整'''
    pass


#注册管理模型类
admin.site.register(BookInfo)
admin.site.register(HeroInfo)