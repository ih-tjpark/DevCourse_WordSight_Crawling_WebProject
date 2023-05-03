from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from new_api import models
# Create your views here.
def index(request):
    return render(request, "pages/home.html")

def detail(request, news_id):
    return render(request, "pages/detail.html", {"news_id": news_id})

def more(request):
    return render(request, "pages/more.html")

def error404view(request, exception=None):
    return render(request, 'pages/404page.html')

def search(request):
    if request.method == "GET":
        keyword = request.GET.get('q')
        if keyword:
            return render(request, "pages/insight.html", {"keyword": keyword})
        else:
            return render(request, "pages/home.html")