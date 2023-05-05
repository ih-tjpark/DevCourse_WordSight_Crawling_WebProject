from functools import reduce
from urllib.parse import urlparse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from new_api.models import News, Keyword, Tag
from new_api.keyword_analysis import get_relation_keyword
from django.template.loader import render_to_string
import requests
#from .forms import InterestTagWidget
#from .models import TagInterest, TagAgency, TagChoices
# Create your views here.
def index(request):
    news = News.objects.all()[:10]
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    context = {'news': news, 'trend_keyword': trend_keyword }

    return render(request, "base.html", context)

def detail(request, news_id):
    news = get_object_or_404(News, news_id=news_id)
    context = {'news': news}
    return render(request, "pages/detail.html", context)

def updateNews(request):
    url = "http://127.0.0.1:8000/news_api/search/"
    params = dict()
    if request.GET.getlist('tags'):
        params["tags"] = params.get("tags", "") + ",".join(request.GET.getlist('tags'))
    if request.GET.getlist('agencys'):
        params["agencys"] = params.get("agencys", "") + ",".join(request.GET.getlist('agencys'))
    response = requests.get(url, params=params)
    news_obj = response.json()["results"]

    tag_list = params['tags'].split(',')
    tag = Tag.objects.filter(class1=tag_list[0])
    #print(params['tags'].split(','))
    print(tag[0].news_set.all())
    #news_obj = tag
    news_obj = tag[0].news_set.all()
    
    rendered = render_to_string("partial/newsDisplay.html", {"news": news_obj})
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
            context= {"keyword": keyword, "relation_keyword":relation_keyword, "news":news, 'trend_keyword':trend_keyword }

            if relation_keyword:
                return render(request, "pages/insight.html", context)
            else:
                return render(request, "pages/emptyWord.html")
        else:
            return render(request, "base.html")
