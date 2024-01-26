from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.http.request import HttpRequest
from .models import AuthToken
from django.contrib.auth import authenticate
from rest_framework import status
import logging

logger = logging.getLogger(__name__)    #logging 

'''
-POST-> View for primary user authentication
     :Responses:
          *HTTP_406_NOT_ACCEPTABLE==> Invalid JSON data
          *HTTP_401_UNAUTHORIZED)==> Wrong password or username
          *HTTP_200_OK ==> Successfull user authentication
-GET-> View for basic user information
'''
class PrimaryAuthView(views.APIView):
     
     def post(self,request:HttpRequest , *args, **kwargs):
          
          request_data = request.data
          
          #extracting request data
          try:
               username = request_data.get("username")
               password = request_data.get("password")
               print(f"{username}, {password}")
          except Exception as e:
               logger.critical(f"EXCEPTION: {e}")
               return Response({
                         "satus":"not_acceptable"   
                    },status=status.HTTP_406_NOT_ACCEPTABLE
               )
          
          #Authenticating user credentials
          user_auth = authenticate(request=request, password = password, username=username)
          if(user_auth is None):        #wrong credentials
               logger.error("This user doesnt exist...")
               return Response({
                    "status":"unautharized"
               }, status=status.HTTP_401_UNAUTHORIZED)
               
          
          return Response(
               {"user":user_auth.get_username()},
               status=status.HTTP_200_OK
          )
          