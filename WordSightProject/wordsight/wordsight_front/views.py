from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from new_api.models import News,Keyword
from new_api.keyword_analysis import get_relation_keyword
from django.template.loader import render_to_string
#from .forms import InterestTagWidget
#from .models import TagInterest, TagAgency, TagChoices
# Create your views here.
def index(request):
    news = News.objects.all()[:12]
    trend_keyword = Keyword.objects.all().order_by('-count')[:10]
    context = {'news': news, 'trend_keyword': trend_keyword }
    return render(request, "base.html", context)

def home(request):
    news = News.objects.all()[:12]
    context = {'news': news}
    return render(request, "pages/home.html", context)

def detail(request, news_id):
    news = get_object_or_404(News, news_id=news_id)
    context = {'news': news}
    return render(request, "pages/detail.html", context)

def updateNews(request, search_key):
    rendered = render_to_string("partial/newsDisplay.html", {"news": News.objects.all()[:12]})
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
