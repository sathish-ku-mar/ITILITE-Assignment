from django.contrib import admin

# Register your models here.
from .models import Theater, Seat_Class, Screen, Movie, Show, Booking


admin.site.register(Theater)
admin.site.register(Seat_Class)
admin.site.register(Screen)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Booking)