import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from .forms import BookInfoForm
from .models import BookInfo,HeroInfo


class IndexView(View):
    def get(self,request):
        context = {
            "city":"beijing",
            "alist":[1,2,3],
            'adict':{
                'name': 'python'
            }
        }
        return render(request,"index.html",context)


class BookView(View):
    def get(self,request):
        form = BookInfoForm()
        print(1,form)
        return render(request,'book.html',{'form':form})
    def post(self,request):
        form = BookInfoForm(request.POST)
        #表单验证
        if form.is_valid():
            print(2,form.cleaned_data)
            return HttpResponse('ok')
        else:
            return render(request, 'book.html', {'form': form})
from datetime import datetime

#REST API  JSON
class BooksAPIView(View):
    def get(self,request):
    # GET   /books/   获取所有图书信息
        books = BookInfo.objects.all()
        #转换
        books_list = []
        for book in books:
            books_list.append({
                'id':book.id,
                'btitle':book.btitle,
                'bpub_date':book.bpub_date.strftime("%Y-%m-%d"),
                'bread':book.bread,
                'bcomment':book.bcomment,
                 'logo':book.logo.url if book.logo else ''
            })

        return JsonResponse(books_list,safe = False)

    def post(self,request):
        # POST   /books/   新增图书信息
        #获取参数
        json_bytes = request.body
        # 转换格式
        json_str =  json_bytes.decode()
        req_data = json.loads(json_str)
        #省略校验参数
        book = BookInfo.objects.create(
            btitle=req_data.get('btitle'),
            bpub_date=datetime.strptime(req_data.get('bpub_date'), '%Y-%m-%d').date()
        )
        #转换
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date.strftime("%Y-%m-%d"),
            'bread': book.bread,
            'bcomment': book.bcomment,
            'logo': book.logo.url if book.logo else ''
        }
        return JsonResponse(book_dict,status=201)

class BookAPIView(View):
    def get(self,request,pk):
    #GET   /books/<pk>/   获取单一图书信息
        try:
            book = BookInfo.objects.get(pk = pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
            # 转换
        book_dict = {
        'id': book.id,
        'btitle': book.btitle,
        'bpub_date': book.bpub_date.strftime("%Y-%m-%d"),
        'bread': book.bread,
        'bcomment': book.bcomment,
        'logo': book.logo.url if book.logo else ''
    }
        return JsonResponse(book_dict)

    def put(self,request,pk):
    #PUT   /books/<pk>/   更新图书信息
        #判断数据是否存在
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        # 转换格式

        json_str = json_bytes.decode()
        req_data = json.loads(json_str)
        # 省略校验参数

        book.btitle=req_data.get('btitle')
        book.bpub_date=datetime.strptime(req_data.get('bpub_date'), '%Y-%m-%d').date()
        book.save()
        # 转换
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date.strftime("%Y-%m-%d"),
            'bread': book.bread,
            'bcomment': book.bcomment,
            'logo': book.logo.url if book.logo else ''
        }
        return JsonResponse(book_dict, status=201)
    def delete(self,request,pk):
        #DELETE   /books/<pk>/   删除图书信息
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        book.delete()
        return HttpResponse(status=200)











