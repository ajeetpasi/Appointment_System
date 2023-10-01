from django.db import models
from django.utils import timezone

# Create your models here.
class DoctorsDetails(models.Model):

    name = models.CharField(max_length=100,default="",blank=False,null=False, help_text="Doctor's Name")

    pincode = models.IntegerField(default=None, help_text="Pincode in which doctor operates")

    start_datetime = models.TimeField(default=timezone.now, help_text="Start Time When doctor sits in the clinic")

    end_datetime = models.TimeField(default=timezone.now, help_text="End Time When doctor sits in the clinic")

    booked_slots = models.IntegerField(default=None, help_text="Number of slots already Booked")

    available_slots = models.IntegerField(default=0,blank=False,null=False, help_text="Number of Patients Doctor Check")

    phone_number = models.CharField(max_length=10,default="",blank=False,null=False, help_text="Doctor's Phone Number")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DoctorsDetail'
        verbose_name_plural = 'DoctorsDetails'

class PatientBookings(models.Model):

    name = models.CharField(max_length=100,default="",blank=False,null=False, help_text="Patient's Name")

    phone_number = models.CharField(max_length=10,default="",blank=False,null=False, help_text="Patient's Phone Number")

    age = models.IntegerField(default=None,blank=False,null=False, help_text="Age of Patient")

    gender = models.CharField(max_length=10,default="",blank=False,null=False, help_text="Gender of Patient")

    slot_booked = models.IntegerField(default=None, help_text="slot number booked for patient")

    doctor_appointed = models.ForeignKey('DoctorsDetails', null=True, blank=True, on_delete=models.CASCADE, help_text="Doctor Appointed")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PatientBooking'
        verbose_name_plural = 'PatientBookings'