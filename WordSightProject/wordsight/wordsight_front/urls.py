from django.urls import path
from . import views
from .views import *
app_name = 'WORDSIGHT'

urlpatterns = [
    path('',views.index, name="index"),
    path("search/", views.search, name="search"),
    path('getNews/values=<str:search_key>', views.updateNews, name="getNews"),
    path("<uuid:news_id>/", views.detail, name="detail"),
]

