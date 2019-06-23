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

# 普通的装饰器
#func_demo(request) -> wrapper(request)
# @my_decorator
# def func_demo(request):
#     return HttpResponse()


#url装饰,在路径上就给他装饰了
# class DemoView(View):
#     """类视图：处理注册"""
#
#     # @method_decorator(my_decorator)
#     # def dispatch(self, *args, **kwargs):
#     #     return super().dispatch(*args, **kwargs)
#
#     def get(self, request):
#         """处理GET请求，返回注册页面"""
#         return HttpResponse("get")
#
#     def post(self, request):
#         """处理POST请求，实现注册逻辑"""
#         return HttpResponse('POST')
#



# 为全部请求方法添加装饰器   类装饰
#name 参数 是给类里面的哪个方法加上装饰
# @method_decorator(my_decorator, name='dispatch')
# class DemoView(View):
#     """类视图：处理注册"""

    # @method_decorator(my_decorator)  经过 method_decorator() 将my_decorator  转换成 函数使用的方法
    # method_decorator()  告诉函数第一个参数是self 对象,不是request请求
    # dispatch  继承as_view里的dispatch方法 可以给下面的请求方法全部都加入装饰范围
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # def get(self, request):
    #     """处理GET请求，返回注册页面"""
    #     return HttpResponse("get")
    #
    # def post(self, request):
    #     """处理POST请求，实现注册逻辑"""
    #     return HttpResponse('POST')


#给类视图使用的 调整后
def my_decorator_for_class(view_func):
    def wrapper(self,request,*args,**kwargs):
        print("装饰器被调用")
        print(request.path)
        return view_func(self,request,*args,**kwargs)
    return wrapper


class DemoView(View):
    """类视图：处理注册"""
    #调整后的装饰器不需要method_decorator()
    @my_decorator_for_class
    def get(self, request):
        """处理GET请求，返回注册页面"""
        return HttpResponse("get")

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('POST')