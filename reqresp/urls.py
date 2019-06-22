from django.conf.urls import url

from . import views

urlpatterns = [

    # url(r'^weather/([a-z]+)/(\d{4})$',views.weather)
    #下面这个办法可以不按参数顺序传入weather函数
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})$',views.weather)
]