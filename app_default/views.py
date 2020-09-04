from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app_default.models import Project, Job, History
from app_default.serializers import DefaultSerializer


class ProjectList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Project.objects.all()
    serializer_class = DefaultSerializer


class JobList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Job.objects.all()
    serializer_class = DefaultSerializer


class HistoryList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = History.objects.all()
    serializer_class = DefaultSerializer
