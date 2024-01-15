from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status
# from .models import AuthToken
import logging

logger = logging.getLogger(__name__)    #logging 

'''
-POST-> View for primary user authentication
     :Responses:
          *HTTP_406_NOT_ACCEPTABLE==>Invalid JSON data
          *
-GET-> View for basic ser information
'''
class PrimaryAuthView(views.APIView):
     def post(self,request:HttpRequest , *args, **kwargs):
          
          request_data = request.data
          
          #extracting request data
          try:
               username = request_data.username
               password = request_data.password
               print(f"{username}, {password}")
          except Exception as e:
               logger.critical(f"EXCEPTION: {e}")
               return Response(
                    status=status.HTTP_406_NOT_ACCEPTABLE
               )
          
          
          
          return Response(
               {"data":request_data},
               status=status.HTTP_200_OK
          )
          