from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from new_api.models import News
from new_api.keyword_analysis import get_relation_keyword
from django.template.loader import render_to_string
#from .forms import InterestTagWidget
#from .models import TagInterest, TagAgency, TagChoices
# Create your views here.
def index(request):
    news = News.objects.all()[:12]
    context = {'news': news}
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

#def modelmultiplechoicefield(request):
#    form = InterestTagWidget(request.POST or None)
#    if request.POST and form.is_valid():
#        tags_interest=form.cleaned_data['tags_interest']
#        tags_agency=form.cleaned_data['tags_agency']
#        obj = TagChoices(tags_interest=tags_interest, tags_agency=tags_agency)
#        obj.save()
#        form2 = InterestTagWidget(request.POST, instance=obj)
#        form2.save(commit=False)
#        form2.save_m2m()
#        return redirect('home')
#    context = {'form':form}
#    return render(request, 'partial/newsDisplay.html',context)