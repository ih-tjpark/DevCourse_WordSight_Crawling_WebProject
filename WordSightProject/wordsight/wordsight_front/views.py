from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "pages/home.html")

def insight(request, keyword):
    return render(request, "pages/insight.html", {"keyword": keyword})

def detail(request, news_id):
    return render(request, "pages/detail.html", {"news_id": news_id})