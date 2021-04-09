from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'nationality', 'passport', 'checkin', 'checkout', 'roomtype')


admin.site.register(Booking, BookingAdmin)
