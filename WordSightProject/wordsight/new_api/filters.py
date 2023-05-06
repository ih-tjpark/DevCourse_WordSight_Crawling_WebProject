import json
from django_filters import rest_framework
import django_filters
from .models import News
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