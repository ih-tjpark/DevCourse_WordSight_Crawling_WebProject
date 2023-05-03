from django.urls import path
from . import views
from .views import *

app_name = 'WORDSIGHT'

urlpatterns = [
    path('',views.index, name="index"),
    path("more/", views.more, name="more"),
    path("search/", views.search, name="search"),
    path("<uuid:news_id>/", views.detail, name="detail"),
]

