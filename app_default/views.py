from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app_default.serializers import *


class ProjectList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class JobList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Job.objects.all()
    serializer_class = JobSerializer


class HistoryList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = HistorySerializer

    def get_queryset(self):
        if 'category' in self.kwargs:
            return History.objects.filter(category=self.kwargs['category'])
        
        return History.objects.all()
