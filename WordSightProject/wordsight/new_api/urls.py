from django.urls import path
from .views import *


app_name = 'new_api'
urlpatterns = [
    path('', NewsList.as_view(), name='news_list')
]
