# Generated by Django 2.2.4 on 2019-08-29 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSeatClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost_per_ticket', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='cost_per_ticket',
        ),
        migrations.DeleteModel(
            name='EventBooking',
        ),
        migrations.AddField(
            model_name='eventseatclass',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
    ]
