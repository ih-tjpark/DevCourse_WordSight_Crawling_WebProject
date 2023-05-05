from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from new_api.models import News
from rest_framework import generics
from new_api.keyword_analysis import get_relation_keyword
from django.template.loader import render_to_string
from new_api.serializers import NewsSerializer
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 10000

class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        response.data['page_obj'] = self.paginator.page
        return response

def index(request):
    news_list = NewsList.as_view()(request).data['results']
    page_obj = NewsList.as_view()(request).data['page_obj']
    context = {'news_list': news_list, 'page_obj': page_obj}
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
            if relation_keyword:
                return render(request, "pages/insight.html", {"keyword": keyword, "relation_keyword":relation_keyword})
            else:
                return render(request, "pages/emptyWord.html")
        else:
            return render(request, "pages/home.html")
