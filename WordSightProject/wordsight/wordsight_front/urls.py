from django.urls import path
from . import views
from .views import *
app_name = 'WORDSIGHT'

urlpatterns = [
    path('',views.index, name="index"),
    path("page/", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("detail/", views.detail, name="detail"),
    path("getNews/", views.updateNews, name="getNews"),
    path('getNews/<str:tag>/', views.updateNews, name='update_news_tag'),
    path("<uuid:news_id>/", views.detail, name="detail"),
]

