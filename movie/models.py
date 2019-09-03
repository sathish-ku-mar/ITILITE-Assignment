from django.db import models
from account.models import User

# Create your models here.


class Theater(models.Model):

    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Theater)


class Screen(models.Model):

    name = models.CharField(max_length=200)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Seat_Class(models.Model):

    name = models.CharField(max_length=200)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True, blank=True)
    cost_per_ticket = models.FloatField()
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):

    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    cast = models.CharField(max_length=200,null=True, blank=True)
    director = models.CharField(max_length=200,null=True, blank=True)
    producer = models.CharField(max_length=200,null=True, blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Show(models.Model):

    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, null=True, blank=True, related_name='shows_screen')
    date = models.DateField()
    time = models.TimeField()
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='shows')
    seat_class = models.ForeignKey(Seat_Class, on_delete=models.CASCADE, related_name='shows_seat_class')
    seat_number = models.CharField(max_length=255)
    no_of_tickets = models.FloatField()
    service_fee = models.FloatField(default=0.0)
    total_cost = models.FloatField(default=0.0)

    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
      return str(self.id)