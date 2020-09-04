from django.urls import path

from .views import *

urlpatterns = [
    path('/project', ProjectList.as_view()),
    path('/job', JobList.as_view()),
]