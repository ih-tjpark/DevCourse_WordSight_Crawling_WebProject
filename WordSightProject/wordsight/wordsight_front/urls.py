from django.urls import path
from . import views
from .views import *

app_name = 'WORDSIGHT'

urlpatterns = [
    path('',views.index, name="index"),
    path("<str:keyword>/", views.detail, name="detail"),
    path("?search=<str:keyword>/", views.detail, name="detail")
]