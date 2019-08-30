from django.db import models

# Create your models here.
from account.models import User


class EventType(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Event(models.Model):

    name = models.CharField(max_length=200)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name='event_type')
    language = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    duration = models.FloatField(default=0.0)
    place = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    event_cost = models.FloatField(default=0.0)
    total_seats = models.IntegerField()
    avilable_seats = models.IntegerField()
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class EventSeatClass(models.Model):

    name = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    cost_per_ticket = models.FloatField()
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class EventBooking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='shows')
    seat_class = models.ForeignKey(EventSeatClass, on_delete=models.CASCADE, related_name='shows_seat_class')
    seat_number = models.CharField(max_length=255)
    no_of_tickets = models.FloatField()
    service_fee = models.FloatField(default=0.0)
    total_cost = models.FloatField(default=0.0)

    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
      return str(self.id)