from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    index视图
    :param request:  包含了请求信息的请求对象
    :return: 响应对象
    '''
    return HttpResponse("hello world")