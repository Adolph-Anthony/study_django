from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
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
    print('-----------------')

    # 表单格式
    # c = request.POST.get('c')
    # d = request.POST.get('d')
    # clist = request.POST.getlist('c')
    # print(c,d,clist)
    # #请求体里获取   c=4&c=5&d=6
    # print(request.body)

    # JSON
    json_bytes = request.body
    json_str = json_bytes.decode()
    # 前端发来的请求的字典数据
    req_dict = json.loads(json_str) #跟python3.6  str  bytes   python3.5只支持str
    c = req_dict.get('c')
    d = req_dict.get('d')
    print(c)
    print(d)
    #获取请求头
    print(request.META.get('CONTENT_LENGTH'))

    # HttpRequest对象的属性GET、POST都是QueryDict类型的对象
    return HttpResponse("OK")

def demo_response(request):
    # s = '{"name":"python"}'
    # response = HttpResponse(s,content_type="application/json",status=200)
    # response["Itcast"] ="python"
    # return response构造

    #Session操作
    request.session["user_id"] = 100
    request.session["userNname"] = "python"
    request.session["user_test"] = "test"
    # 以键获取session的值
    print(request.session.get('user_id', None))
    # 设置session有效值 以秒计算
    # request.session.set_expiry(10)

    #快速构建json格式数据
    return JsonResponse({'city': 'beijing', 'subject': 'python'})