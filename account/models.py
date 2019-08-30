from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from core.common import (mobile_regex)

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    email = models.EmailField()
    password = models.TextField()
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES,
                              default='Male')
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def __str__(self):
        return self.name