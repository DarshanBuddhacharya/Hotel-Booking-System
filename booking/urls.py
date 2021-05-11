from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact.html/', views.contact),
    path('form.html/', views.form),
    path('form.html/', views.Booking),
    path('accommodation.html/', views.accommodation),
    path('help.html/', views.help),
    path('booked.html/', views.booked),
    path('cancelForm.html/', views.cancelForm),
    path('conCancel.html/', views.conCancel),
    path('footer.html/', views.footer)
]
