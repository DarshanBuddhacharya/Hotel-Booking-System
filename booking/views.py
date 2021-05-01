from django.http import HttpResponse
from django.shortcuts import render
from booking.models import Booking
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def accommodation(request):
    return render(request, 'accommodation.html')


def form(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('address') and request.POST.get(
            'nationality') and request.POST.get('passport') and request.POST.get('phnumber') and request.POST.get(
                'checkin') and request.POST.get('checkout') and request.POST.get('roomtype'):
            saverecord = Booking()
            saverecord.name = request.POST.get('name')
            saverecord.address = request.POST.get('address')
            saverecord.nationality = request.POST.get('nationality')
            saverecord.passport = request.POST.get('passport')
            saverecord.phnumber = request.POST.get('phnumber')
            saverecord.checkin = request.POST.get('checkin')
            saverecord.checkout = request.POST.get('checkout')
            saverecord.roomtype = request.POST.get('roomtype')
            saverecord.save()
            messages.success(request, "Booking submitted successfully")
    return render(request, 'form.html')


def help(request):
    return render(request, 'help.html')


def booked(request):
    return render(request, 'booked.html')


def cancel(request):
    return render(request, 'cancel.html')


def confirm(request):
    return render(request, 'confirm.html')
