from django.shortcuts import render
from rest_framework.views import APIView
from django.http.request import HttpRequest
from rest_framework.response import Response
# from user.models import UserProfile
from django.contrib.auth.models import User
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

'''
-POST-> View for primary user regstration
     :Responses:
          *HTTP_406_NOT_ACCEPTABLE==>Invalid JSON data
          
'''
class UserRegistration(APIView):
     def post(self, request:HttpRequest ,*args, **kwargs):
          request_data = request.data
          
          #extracting request data
          try:
               username = request_data.username
               password = request_data.password
               dob = request_data.dob
               email = request.email
               
          except Exception as e:
               logger.error(f"EXCEPTION: {e}")
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE)   
          
          #user creation
          User.objects.create_user(
               username=username,
               email=email,
               password=password
          )
          
          
