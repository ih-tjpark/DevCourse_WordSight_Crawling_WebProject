from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from new_api.models import News
from new_api.keyword_analysis import get_relation_keyword

# Create your views here.
def index(request):
    news = News.objects.all()[:12]
    context = {'news': news}
    return render(request, "pages/home.html", context)

def detail(request, news_id):
    news = get_object_or_404(News, news_id=news_id)
    context = {'news': news}
    return render(request, "pages/detail.html", context)

def more(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, "pages/more.html", context)

def error404view(request, exception=None):
    return render(request, 'pages/404page.html')

def search(request):
    if request.method == "GET":
        keyword = request.GET.get('q')
        if keyword:
            relation_keyword = get_relation_keyword(keyword)
            return render(request, "pages/insight.html", {"keyword": keyword, "relation_keyword":relation_keyword})
        else:
            return render(request, "pages/home.html")

