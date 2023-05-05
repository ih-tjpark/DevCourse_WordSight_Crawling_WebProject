from .models import *
from .serializers import *
from .paginators import *
from rest_framework import generics, filters
from rest_framework.response import Response
import django_filters 
from django_filters import rest_framework as filters 
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .filters import *


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


class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


class SearchViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [WordFilter]

class NewsDetail(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

class KeywordList(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

