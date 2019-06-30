import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .forms import BookInfoForm
from .models import BookInfo,HeroInfo
from .serializers import BookInfoSerializer

# GET /books/
# class BookListAPIView(APIView):
#     def get(self,request):
#         #数据库查询方法
#         querySet = BookInfo.objects.all()
#
#         #构建序列化器对象,进行序列化操作
#         seializer = BookInfoSerializer(querySet,many=True)
#
#         # seializer.data
#         return Response(seializer.data,status=200)
#

# GET /books/   继承GenericAPIView
# class BookListAPIView(GenericAPIView):
#     # 数据库查询方法
#     queryset = BookInfo.objects.all()
#     #序列化
#     serializer_class = BookInfoSerializer
#     def get(self,request):
#         #数据库查询方法
#         qs = self.get_queryset()
#         #构建序列化器对象,进行序列化操作
#         # seializer = BookInfoSerializer(querySet,many=True)
#         seializer = self.get_serializer(qs,many =True)
#         # seializer.data
#         return Response(seializer.data,status=200)

#简化序列化 扩展类mixins.ListModelMixin
from rest_framework import mixins
# class BookListAPIView(mixins.ListModelMixin,GenericAPIView):
#     # 数据库查询方法
#     queryset = BookInfo.objects.all()
#     #序列化
#     serializer_class = BookInfoSerializer
#     def get(self,request):
#         #序列化过程全在list里,
#         return self.list(request)
#
# # GET /books/<pk>
# class BookDetailAPIView(GenericAPIView):
#     # 数据库查询方法
#     queryset = BookInfo.objects.all()
#     #序列化
#     serializer_class = BookInfoSerializer
#     def get(self,request,pk):
#         #数据库查询方法
#         book = self.get_object()
#         #构建序列化器对象,进行序列化操作
#         seializer = self.get_serializer(book)
#         # seializer.data
#         return Response(seializer.data,status=200)
#
#

#视图集
from rest_framework.viewsets import GenericViewSet
class BookInfoViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


