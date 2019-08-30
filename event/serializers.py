from rest_framework import serializers
from .models import Event, EventSeatClass, EventBooking


class EventSeatClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventSeatClass
        fields = ('id', 'name', 'cost_per_ticket')


class EventSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name')

    class Meta:
        model = Event
        fields = ('id', 'name', 'type', 'language', 'date', 'time', 'duration', 'place', 'address', 'artist')


class EventBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventBooking
        fields = ('id', 'user', 'event', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost')


class EventBookingListSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=False)
    seat_class = EventSeatClassSerializer(read_only=True, many=False)

    class Meta:
        model = EventBooking
        fields = ('id', 'user', 'event', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost')