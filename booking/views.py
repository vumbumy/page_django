from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from booking.models import Booking
from booking.serializers import BookingSerializer

from .permissions import *


class BookingList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsOwnOnly)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
