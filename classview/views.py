from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
# Create your views here.

def my_decorator(view_func):
    def wrapper(request,*args,**kwargs):
        print("装饰器被调用")
        print(request.path)
        return view_func(request,*args,**kwargs)
    return wrapper

#func_demo(request) -> wrapper(request)
# @my_decorator
# def func_demo(request):
#     return HttpResponse()



# 为全部请求方法添加装饰器
@method_decorator(my_decorator, name='dispatch')
class DemoView(View):
    """类视图：处理注册"""


    # @method_decorator(my_decorator)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)



    def get(self, request):
        """处理GET请求，返回注册页面"""
        return HttpResponse("get")

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('POST')
