from django.urls import path
from .views import *


app_name = 'new_api'
urlpatterns = [
    path('search/', SearchViewSet.as_view({'get': 'list'}), name='search'),
    path('', NewsList.as_view(), name='news_list'),
]
