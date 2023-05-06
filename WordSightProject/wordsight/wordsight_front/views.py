from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from new_api.models import News, Keyword, Tag
from new_api.models import News, Keyword, Tag
from new_api.views import NewsList
from new_api.keyword_analysis import get_relation_keyword
from django.template.loader import render_to_string
from new_api.filters import NewsFilter
# from rest_framework import generics
# import requests
# from new_api.serializers import NewsSerializer
# from rest_framework.pagination import PageNumberPagination
# from django.db.models import Q,QuerySet


def index(request):
    news_list = NewsList.as_view()(request).data['results']
    page_obj = NewsList.as_view()(request).data['page_obj']
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    context = {'news_list': news_list, 'page_obj': page_obj, 'trend_keyword': trend_keyword }
    
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    context = {'news_list': news_list, 'page_obj': page_obj, 'trend_keyword': trend_keyword }

    return render(request, "base.html", context)

def detail(request, news_id):
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    news = get_object_or_404(News, news_id=news_id)
    tag = news.tag.all()
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    context = {'news': news, 'tag': tag, 'trend_keyword': trend_keyword}
    return render(request, "pages/detail.html", context)

def updateNews(request):
    url = "http://127.0.0.1:8000/news_api/search/"
    params = dict()

    if request.GET.getlist('tags'):
        params["tags"] = params.get("tags", "") + ",".join(request.GET.getlist('tags'))


    if request.GET.getlist('agencys'):
        params["agencys"] = params.get("agencys", "") + ",".join(request.GET.getlist('agencys'))      
    
    test = NewsFilter(params['tags'], params['agencys'])
    news_obj=test.get_news()

    print(params)
    #print(news_obj)

    rendered = render_to_string("partial/newsDisplay.html", {"news_list": news_obj})
    return HttpResponse(rendered, content_type="text/plain")

def error404view(request, exception=None):
    return render(request, 'pages/404page.html')

def search(request):
    if request.method == "GET":
        keyword = request.GET.get('q')
        if keyword:
            relation_keyword = get_relation_keyword(keyword)
            keyword = Keyword.objects.get(name=keyword)
            news = keyword.news_set.all()
            trend_keyword = Keyword.objects.all().order_by('-count')[:10]
            tag= Tag.objects.none()
            for n in news:
                tag = tag | n.tag.all()

            context= {"keyword": keyword, "relation_keyword":relation_keyword, "news":news, 'trend_keyword':trend_keyword, 'tag':tag }

            if relation_keyword:
                return render(request, "pages/insight.html", context)
            else:
                return render(request, "pages/emptyWord.html")
        else:
            return render(request, "base.html")

def page(request):
    return HttpResponse("page")
