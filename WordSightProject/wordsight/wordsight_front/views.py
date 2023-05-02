from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "home.html")

def detail(request, keyword):
    return render(request, "detail.html", {"keyword": keyword})