import json
from django_filters import rest_framework
import django_filters
from .models import *
from rest_framework import filters
from django.db.models import Q

class MultiValueCharFilter(rest_framework.BaseCSVFilter, rest_framework.CharFilter):
    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs
class TagFilter(django_filters.FilterSet):
    interest__contains = MultiValueCharFilter(name='tag', lookup_expr='contains')
    class Meta:
        models = News
        search_fields = ["__all__"]

class WordFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        tags = request.query_params.get('tags', "")
        agencys = request.query_params.getlist('agencys', [""])[0]
        news_filter = Q()
        if tags:
            for tag in tags.split(','):
                news_filter |= Q(tag_list__contains=tag)
        if agencys:
            for agency in agencys.split(','):
                news_filter |= Q(news_agency=agency)
        queryset = queryset.filter(news_filter)
        print(queryset)
        return queryset

    def filter_instance(self, instance):
        jsonDec = json.decoder.JSONDecoder()
        decoded_tag_list = jsonDec.decode(instance.tag_list) if instance.tag_list is not None else []
        instance.tag_list = decoded_tag_list
        return instance

class NewsFilter:
    def __init__(self, tag, agency):
        self.tag = tag
        self.agency = agency

    def get_news(self): 
        news = News.objects.none()
        
        if self.tag or self.agency:
            if self.tag:
                tag_list = self.tag.split(',')
                news_tag = News.objects.none()
                for tag in tag_list[::-1]:
                    tag_object_set = Tag.objects.filter(class1 = tag)
                    #print(tag_object_set)
                    for tag_object in tag_object_set:
                        news_tag = news_tag | tag_object.news_set.all()[:10]
                news = news_tag
                print('tag실행')

            if self.agency:
                agency_list = self.agency.split(',')
                news_agency = News.objects.none()
                for agency in agency_list[::-1]:
                    news_object_set = News.objects.filter(news_agency = agency)[:10]
                    news_agency = news_agency | news_object_set
                news = news_agency
                print('agency실행')

            if  self.tag != '' and self.agency != '':
                print("and 실행")
                news = news_tag & news_agency
        
        else:
            news = News.objects.all().order_by('-created_date')[:100]

        return news
    