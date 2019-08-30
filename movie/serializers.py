from rest_framework import serializers
from .models import Theater, Seat_Class, Movie, Show, Booking


class Seat_ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat_Class
        fields = ('id', 'name', 'cost_per_ticket')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'name', 'language')


class TheaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theater
        fields = ('id', 'name', 'place', 'address')


class ShowSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer(read_only=True, many=False)
    movie = MovieSerializer(read_only=True, many=False)
    screen = serializers.CharField(source='screen.name')

    class Meta:
        model = Show
        fields = ('theater', 'movie', 'screen', 'date', 'time')


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'user', 'show', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost')


class BookingListSerializer(serializers.ModelSerializer):
    show = ShowSerializer(read_only=True, many=False)
    seat_class = Seat_ClassSerializer(read_only=True, many=False)

    class Meta:
        model = Booking
        fields = ('id', 'user', 'show', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost')