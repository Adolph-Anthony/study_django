from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^demoview$', views.DemoView.as_view()),

    # 在url中添加装饰器,最简单但不利于代码完整性,不建议
    # url(r'^demoview$', views.my_decorator(views.DemoView.as_view())),

    # 在类视图中装饰   views.DemoView.as_view()  调用类视图
    url(r'^demoview$',views.DemoView.as_view()),

]

