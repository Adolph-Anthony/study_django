from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, HeroInfo

#注册管理模型类
admin.site.register(BookInfo)
admin.site.register(HeroInfo)