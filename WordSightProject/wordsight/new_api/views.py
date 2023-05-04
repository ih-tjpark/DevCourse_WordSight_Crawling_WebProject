from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from .paginators import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


# Home:뉴스 목록 9개씩 보여주는 역할 - GET
class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'newsCard.html'
    # def get(self, request):
    #     queryset = News.objects.all().order_by('-created_date')
    #     # serializer_class = NewsSerializer
    #     return Response({'news': queryset})

# 뉴스 상세보기 역할
class NewsDetail(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

# 키워드 목록 보여주는 역할
class KeywordList(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

# 주요 관련 키워드 보여주는 역할


# 