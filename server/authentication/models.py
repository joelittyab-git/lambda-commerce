from django.db import models
from django.contrib.auth.models import User
import binascii
import os

'''
Table for user authentication and token
Relation:
     O->O => django.contrib.auth.models.User
'''  
class AuthToken(models.Model):
     token_id = models.BigAutoField(primary_key=True)
     token_key = models.CharField(max_length=100, unique=True, null=False)
     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add = True)
     
     
     def save(self, user:User):
          key = AuthToken.generate_key()
          self.token_key(f"{key}")
          super().save()
          
     def create(self, user:User):
          self.save(user=user)
     
     @classmethod
     def generate_key(cls):
          return binascii.hexlify(os.urandom(20)).decode()