from django.http import HttpResponse
from django.shortcuts import render
from booking.models import Booking
from django.core.mail import send_mail
from booking.models import Cancel

import random

x = random.randint(100000, 999999)
y = random.randint(100000, 999999)
ranNum = str(x)
ranNum2 = str(y)
num = 3


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def accommodation(request):
    return render(request, 'accommodation.html')


def form(request):
    if request.method == "POST":
        booking = Booking()
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

        send_mail(
            name,
            passport,
            'testproject1345@gmail.com',
            [email],
            fail_silently=False)
        return render(request, 'conBook.html', {'name': name, 'ranNum': ranNum})

    return render(request, 'form.html')


def help(request):
    return render(request, 'help.html')


def ConBook(request):
    return render(request, 'ConBook.html')


def cancelForm(request):
    if request.method == "POST":
        cancel = Cancel()
        name = request.POST.get('name')
        order = request.POST.get('order')
        email = request.POST.get('email')
        verification = request.POST.get('verification')
        phnumber = request.POST.get('phnumber')
        reason = request.POST.get('reason')
        cancel.name = name
        cancel.order = order
        cancel.email = email
        cancel.verification = verification
        cancel.phnumber = phnumber
        cancel.reason = reason
        cancel.save()

        send_mail(
            name + "," + " " + "You have sucessfully canceled your Booking",
            "Sorry For Your inconvinace, We understand your reason. Hope you consider us next time" + ranNum,
            'testproject1345@gmail.com',
            [email],
            fail_silently=False)

        return render(request, 'conCancel.html')
    return render(request, 'cancelForm.html')


def conCancel(request):
    return render(request, 'conCancel.html')


def footer(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message_number = request.POST.get('message-number')
        message = request.POST.get('message')

        send_mail(
            message_name,
            message,
            message_email,
            ['testproject1345@gmail.com'],
            fail_silently=False)

        return render(request, 'footer.html', {'message_name': message_name})
    return render(request, 'footer.html')
