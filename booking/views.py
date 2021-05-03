from django.http import HttpResponse
from django.shortcuts import render
from booking.models import HotelBooking


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def accommodation(request):
    return render(request, 'accommodation.html')


def form(request):
    if request.method == "POST":
        booking = HotelBooking()
        name = request.POST.get('name')
        address = request.POST.get('address')
        nationality = request.POST.get('nationality')
        passport = request.POST.get('passport')
        email = request.POST.get('email')
        phnumber = request.POST.get('phnumber')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        roomtype = request.POST.get('roomtype')
        booking.name = name
        booking.address = address
        booking.nationality = nationality
        booking.passport = passport
        booking.email = email
        booking.phnumber = phnumber
        booking.checkin = checkin
        booking.checkout = checkout
        booking.roomtype = roomtype
        booking.save()
        return HttpResponse("<h1>Thanks for Booking</h1>")

    return render(request, 'form.html')


def help(request):
    return render(request, 'help.html')


def booked(request):
    return render(request, 'booked.html')


def cancel(request):
    return render(request, 'cancel.html')


def confirm(request):
    return render(request, 'confirm.html')
