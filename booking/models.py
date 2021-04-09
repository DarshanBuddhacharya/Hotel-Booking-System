from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    phnumber = models.IntegerField
    checkin = models.DateField(max_length=100)
    checkout = models.DateField(max_length=100)
    roomtype = models.CharField(max_length=100)

    class Meta:
        db_table = "booking_booking"
