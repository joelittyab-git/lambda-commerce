from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from django. contrib.auth.models import User

'''
A backend class with aithentication ideals and contrstucts
'''
class AuthBackend(BaseBackend):
     def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
          auth_user = User.objects.filter(username=username)  #fethcing filtered list of any match
          auth_pres = auth_user.exists()
          if(not auth_pres):
               return None
          if(not auth_user.get(username=username).check_password(password)):    #validating password match
               return None
              
          return User.objects.get(username=username)
     
     def get_user(self, user_id: int) -> AbstractBaseUser | None:
          return super().get_user(user_id)