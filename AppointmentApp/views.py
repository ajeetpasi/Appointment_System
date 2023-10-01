from django.shortcuts import render
from django.http import HttpResponse
from AppointmentApp.models import *
import datetime
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
import sys

# Logger
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

def index(request):
    return HttpResponse("Hey, welcome to the <b>Ajeet</b> Appointment App.")


class GetDoctorDetailsAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        response = {}
        response['status'] = 500
        try:
            try:
                data = request.data
            except:
                response['status'] = 400
                response['message'] = "Malformed request body."
                return Response(data=response, status=response['status'])

            pincode = ""
            if 'pincode' in data:
                pincode = data['pincode']
                if len(pincode) != 6:
                   response['status'] = 400
                   response['message'] = "Please enter a vaild pincode."
                   return Response(data=response, status=400) 

            try:
                doctor_objs = DoctorsDetails.objects.filter(pincode = int(pincode))
                if len(doctor_objs) == 0:
                    response['status'] == 200
                    response['message'] = "No Doctors are available in your area, try to search for a different area."
                    return Response(data=response, status=200)
                doctor_list = []
                i = 0
                for objs in doctor_objs:
                    doctor = {}
                    doctor['name'] = objs.name
                    doctor['phone_number'] = objs.phone_number
                    start_time = objs.start_datetime
                    start_time = start_time.strftime("%I:%M %p")
                    start_time = start_time.replace(":00", "") 
                    end_time = objs.end_datetime
                    end_time = end_time.strftime("%I:%M %p")
                    end_time = end_time.replace(":00", "") 
                    doctor['availability'] = f"Doctor's timings: From {start_time} to {end_time}"
                    doctor['number_of_patients_doctor_check'] = objs.available_slots
                    doctor['slots_booked'] = objs.booked_slots
                    doctor_list.append(doctor)
                response['status'] = 200
                response['message'] = "Success"
                response['doctors_details'] = doctor_list
                return Response(data=response, status=response['status'])
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                logger.error("GetDoctorDetailsAPI Error: %s at %s", e, str(
                    exc_tb.tb_lineno), extra={'AppName': 'AppointmentApp'})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error("GetDoctorDetailsAPI: %s at %s", e, str(
                exc_tb.tb_lineno), extra={'AppName': 'AppointmentApp'})

        return Response(data=response, status=response['status'])


GetDoctorDetails = GetDoctorDetailsAPI.as_view()



class PatientSlotBookingAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        response = {}
        response['status'] = 500
        try:
            try:
                data = request.data
            except:
                response['status'] = 400
                response['message'] = "Malformed request body."
                return Response(data=response, status=response['status'])

            name = ""
            if 'name' in data:
                name = data['name']
            if name == "":
                response['status'] = 400
                response['message'] = "Please enter your name , it is a mandatory field."
                return Response(data=response, status=response['status'])
            age = ""
            if 'age' in data:
                age = data['age']
            if age == "":
                response['status'] = 400
                response['message'] = "Please enter your age , it is a mandatory field."
                return Response(data=response, status=response['status'])
            gender = ""
            if 'gender' in data:
                gender = data['gender']
            if gender == "":
                response['status'] = 400
                response['message'] = "Please enter your gender , it is a mandatory field."
                return Response(data=response, status=response['status'])
            phone_number = ""
            if 'phone_number' in data:
                phone_number = data['phone_number']
            if phone_number == "":
                response['status'] = 400
                response['message'] = "Please enter your phone_number , it is a mandatory field."
                return Response(data=response, status=response['status'])
            pincode = ""
            if 'pincode' in data:
                pincode = data['pincode']
                if len(pincode) != 6:
                   response['status'] = 400
                   response['message'] = "Please enter a vaild pincode."
                   return Response(data=response, status=400)
            if pincode == "":
                response['status'] = 400
                response['message'] = "Please enter your pincode , it is a mandatory field."
                return Response(data=response, status=response['status'])

            try:
                doctor_objs = DoctorsDetails.objects.filter(pincode = int(pincode))
                if len(doctor_objs) == 0:
                    response['status'] = 200
                    response['message'] = "No Doctors are available in your area, try to search for a different area."
                    return Response(data=response, status=200)
                for objs in doctor_objs:
                    slots_booked = objs.booked_slots
                    available_slots = objs.available_slots
                    if available_slots == slots_booked:
                        continue
                    slots_booked+=1
                    objs.booked_slots = slots_booked
                    objs.save()
                    doctor_name = objs.name
                    PatientBookings.objects.create(name=name,phone_number = phone_number,age = age,gender=gender,slot_booked=slots_booked, doctor_appointed=objs)
                    break
                response['status'] = 200
                response['message'] = "Your Appointment is booked"
                response['slot_number'] = slots_booked
                response['doctor_appointed'] = doctor_name
                return Response(data=response, status = 200)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                logger.error("GetDoctorDetailsAPI Error: %s at %s", e, str(
                    exc_tb.tb_lineno), extra={'AppName': 'AppointmentApp'})
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error("PatientSlotBookingAPI: %s at %s", e, str(
                exc_tb.tb_lineno), extra={'AppName': 'AppointmentApp'})

        return Response(data=response, status=response['status'])

PatientSlotBooking = PatientSlotBookingAPI.as_view()