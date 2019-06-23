from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^demoview$', views.DemoView.as_view()),

    # 在url中添加装饰器
    url(r'^demoview$', views.my_decorator(views.DemoView.as_view())),

]

