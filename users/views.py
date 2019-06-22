from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    index视图
    :param request:  包含了请求信息的请求对象
    :return: 响应对象
    '''
    return HttpResponse("hello world")


def say(request):
    url = reverse("users:index")
    print(url)
    return HttpResponse("say")


def sayhello(request):
    return HttpResponse("say hello")