from django.urls import path
from . import views
from .views import *

app_name = 'WORDSIGHT'

urlpatterns = [
    path('',views.index, name="index"),
]