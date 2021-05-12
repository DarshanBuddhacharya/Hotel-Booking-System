from django.contrib import admin
from .models import Booking
from .models import Cancel


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'nationality', 'passport', 'email', 'phnumber', 'checkin', 'checkout', 'roomtype')


admin.site.register(Booking, BookingAdmin)


class CancelAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'order', 'email', 'verification', 'phnumber', 'reason')


admin.site.register(Cancel, CancelAdmin)
