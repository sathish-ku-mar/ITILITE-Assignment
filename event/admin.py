from django.contrib import admin
from .models import Event, EventSeatClass, EventBooking, EventType
# Register your models here.

admin.site.register(EventType)
admin.site.register(EventSeatClass)
admin.site.register(Event)
admin.site.register(EventBooking)