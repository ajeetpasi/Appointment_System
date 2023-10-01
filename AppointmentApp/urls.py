from django.urls import re_path
from django.conf import settings
from django.contrib import admin

from AppointmentApp import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^get-doctor-details/$', views.GetDoctorDetails),
    re_path(r'^patient-slot-booking/$', views.PatientSlotBooking),
]