"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import users.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #users充当前缀, users/index
    # url(r'^users/', include("users.urls")) + 命名空间
    url(r'^users/', include("users.urls",namespace="users")),
    #直接视图调用
    # url(r'^index/$', users.views.index)
    #不想加前缀
    url(r'^', include("reqresp.urls")),
    url(r'^', include("classview.urls")),
    url(r'^', include("booktest.urls")),

]
