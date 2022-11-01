from flights.serializers import BookingListSerializer, FlightListSerializer
from .models import Booking, Flight
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.utils import timezone

class FlightListView(ListAPIView):
    queryset=Flight.objects.all()
    serializer_class=FlightListSerializer

class UpcomingBookingListView(ListAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingListSerializer


