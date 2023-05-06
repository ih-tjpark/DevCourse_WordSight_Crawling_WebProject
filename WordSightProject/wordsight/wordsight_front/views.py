from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from new_api.models import News, Keyword, Tag
from new_api.views import NewsList
from new_api.keyword_analysis import get_relation_keyword
from django.template.loader import render_to_string
import requests
from new_api.serializers import NewsSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    news_list = NewsList.as_view()(request).data['results']
    page_obj = NewsList.as_view()(request).data['page_obj']
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    context = {'news_list': news_list, 'page_obj': page_obj, 'trend_keyword': trend_keyword }

    return render(request, "base.html", context)

def detail(request, news_id):
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    news = get_object_or_404(News, news_id=news_id)
    context = {'news': news, "trend_keyword": trend_keyword}
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
    #print(tag[0].news_set.all())
    #news_obj = tag
    #news_obj = tag[0].news_set.all()
    
    rendered = render_to_string("partial/newsDisplay.html", {"news": news_obj})
    return HttpResponse(rendered, content_type="text/plain")

def error404view(request, exception=None):
    return render(request, 'pages/404page.html')

def search(request):
    if request.method == "GET":
        search_key = request.GET.get('q')
        if search_key:
            try:
                keyword = Keyword.objects.get(name=search_key)
                relation_keyword = get_relation_keyword(search_key)
                news = keyword.news_set.all()[:5]
                trend_keyword = Keyword.objects.all().order_by('-count')[:10]
                related_tag =[]
                for each_news in news:
                    related_tag.extend(each_news.tag.all().values_list('class1', flat=True))
                related_tag = list(set(related_tag))[:5]
                date_graph = dict()
                for word in list(keyword.in_date.strip("[]").split(", ")):
                    word = word.strip("\"")
                    date_graph[word] = date_graph.get(word, 0) + 1
                date_graph = sorted(date_graph.items(), key=lambda x: x[0])
                date_graph = [(datetime.strptime(x[0],'%Y-%m-%d').strftime("%m월 %d일").lstrip("0").replace(" 0", " "),
                                x[1]*100//int(keyword.count)) for x in date_graph]
                context= {"keyword": keyword, 
                        "relation_keyword":relation_keyword,
                        "news":news, 
                        'trend_keyword':trend_keyword, 
                        "related_tag":related_tag,
                         "date_graph":date_graph 
                }

                if relation_keyword:
                    return render(request, "pages/insight.html", context)
            except ObjectDoesNotExist:
                return render(request, "pages/emptyWord.html")
        else:
            return render(request, "base.html")

def page(request):
    return HttpResponse("page")
