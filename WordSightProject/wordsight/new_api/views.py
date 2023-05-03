from django.shortcuts import render
from .models import *
from .serializers import *
from .paginators import *
from rest_framework import generics
from rest_framework.response import Response

# Home:뉴스 목록 9개씩 보여주는 역할 - GET
class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

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

# 첫화면은 상위 9개만, 더보기
# 페이지네이션 -> 9씩 쿼리로 



# 키워드 랭킹, 카운트