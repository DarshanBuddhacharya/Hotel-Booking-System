from django.contrib import admin
from .models import HotelBooking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'nationality', 'passport','email','phnumber','checkin', 'checkout', 'roomtype')


admin.site.register(HotelBooking, BookingAdmin)
