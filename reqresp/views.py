from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def weather(request,city,year):
#     print(city)
#     print(year)
#     return HttpResponse("OK")
#

# /weather/beijing/2018/?a=1&b=2&a=3
def weather(request,year,city):
    # print(city)
    # print(year)
    # 查询字符串参数
    #获取到多值时返回最后一个值 a = 3
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')

    print(a,b,alist)
    # HttpRequest对象的属性GET、POST都是QueryDict类型的对象
    return HttpResponse("OK")