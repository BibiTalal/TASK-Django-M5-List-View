from flights.serializers import BookingListSerializer, FlightListSerializer,BookingDetailSerializer,BookingUpdateSerializer
from .models import Booking, Flight
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView


class FlightListView(ListAPIView):
    queryset=Flight.objects.all()
    serializer_class=FlightListSerializer

class UpcomingBookingListView(ListAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingListSerializer

class BookingDetailView(RetrieveAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingUpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'