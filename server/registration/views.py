from django.shortcuts import render
from rest_framework.views import APIView
from django.http.request import HttpRequest
from rest_framework.response import Response
# from user.models import UserProfile
from django.contrib.auth.models import User
from rest_framework import status
import logging
from django.db import IntegrityError

logger = logging.getLogger(__name__)

'''
-POST-> View for primary user regstration
     :Responses:
          *HTTP_406_NOT_ACCEPTABLE==>Invalid JSON data
          
'''
class UserRegistration(APIView):
     def post(self, request:HttpRequest ,*args, **kwargs):
          request_data = request.data
          print(request_data)
          
          #extracting request data
          try:
               username = request_data.get("username")
               password = request_data.get("password")
               dob = request_data.get("dob")
               email = request_data.get("email")
               
          except Exception as e:
               logger.error(f"EXCEPTION: {e}")
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE)   
          
          #user creation
          try:
               User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
               )
          except IntegrityError as e:
               return Response({
                    "status":"Already exists"
               }, status=status.HTTP_409_CONFLICT)
               
               
          user_created = {
               "username":username,
               "email":email,
               "password":password,
               "profile":{
                    
               }
               
          }
          
          return Response(status=status.HTTP_201_CREATED)
          
          
