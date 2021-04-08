from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact.html/', views.contact),
    path('accommodation.html/', views.accommodation)
]
