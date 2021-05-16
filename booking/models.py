from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phnumber = models.BigIntegerField(max_length=12)
    checkin = models.DateTimeField(max_length=15)
    checkout = models.DateTimeField(max_length=15)
    roomtype = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "room_book"


class Cancel(models.Model):
    name = models.CharField(max_length=100)
    order = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    verification = models.CharField(max_length=100)
    phnumber = models.BigIntegerField(max_length=12)
    reason = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cancel_book"
