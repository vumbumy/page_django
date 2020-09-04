from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('project', ProjectList.as_view()),
    path('job', JobList.as_view()),
    path('history', HistoryList.as_view()),
    path('history/<slug:category>', HistoryList.as_view()),
]