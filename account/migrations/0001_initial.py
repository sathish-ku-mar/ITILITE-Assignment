# Generated by Django 2.2.4 on 2019-08-28 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please Enter correct Contact no.', regex='^\\d{10,15}$')])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]