from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from .paginators import *
from rest_framework import generics, filters
from rest_framework.response import Response
import django_filters 
from django_filters import rest_framework as filters 
from rest_framework.pagination import PageNumberPagination

# class CustomPagination(PageNumberPagination):
#     page_size = 12 # 한 페이지에 보여질 개수
#     page_query_param = 'page' # 페이지 번호를 지정할 수 있는 query parameter 이름
#     page_size_query_param = 'page_size' # 한 페이지에 보여질 개수를 지정할 수 있는 query parameter 이름
#     max_page_size = 5000 # 최대 페이지 개수


#
class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    serializer_class = NewsSerializer
    # pagination_class = CustomPagination
    # template_name = 'newsDisplay.html'
    
    # def get(self, request, *args, **kwargs):
    #     queyset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queyset)
        
    #     if page is None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer)
    #     serializer = self.get_serializer(queyset, many=True)
    #     return Response(serializer.data)


class MultiValueCharFilter(filters.BaseCSVFilter, filters.CharFilter):
    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs

class InterestTagFilter(django_filters.FilterSet):
    interest__contains = MultiValueCharFilter(name='tag', lookup_expr='contains')
    class Meta:
        search_fields = ["__all__"]



# 뉴스 상세보기 역할
class NewsDetail(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

# 키워드 목록 보여주는 역할
class KeywordList(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

# 주요 관련 키워드 보여주는 역할