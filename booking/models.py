from django.db import models


class HotelBooking(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phnumber = models.CharField(max_length=100)
    checkin = models.CharField(max_length=100)
    checkout = models.CharField(max_length=100)
    roomtype = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "booking_room"
