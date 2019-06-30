import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import BookInfoForm
from .models import BookInfo,HeroInfo
from .serializers import BookInfoSerializer

# GET /books/
class BookListAPIView(APIView):
    def get(self,request):
        #数据库查询方法
        querySet = BookInfo.objects.all()

        #构建序列化器对象,进行序列化操作
        seializer = BookInfoSerializer(querySet,many=True)

        # seializer.data
        return Response(seializer.data,status=200)

