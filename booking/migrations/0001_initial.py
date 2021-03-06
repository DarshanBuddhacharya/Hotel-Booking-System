# Generated by Django 3.1.7 on 2021-04-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=100)),
                ('checkin', models.DateField(max_length=100)),
                ('checkout', models.DateField(max_length=100)),
                ('roomtype', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'booking_booking',
            },
        ),
    ]
