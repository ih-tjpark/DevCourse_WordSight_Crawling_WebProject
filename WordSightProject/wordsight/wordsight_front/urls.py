from django.urls import path
from . import views
from .views import *

app_name = 'WORDSIGHT'

urlpatterns = [
    path('',views.index, name="index"),
    path("<str:keyword>/", views.insight, name="insight"),
    path("?search=<str:keyword>/", views.insight, name="insight"),
    path("<uuid:news_id>/", views.detail, name="detail"),
    path("more-news/", views.more, name="more")
]