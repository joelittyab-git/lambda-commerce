from django.db import models
from django.contrib.auth.models import User
'''
Describes the basic user 
'''
class UserProfile(models.Model):
     user = models.OneToOneField(to=User, primary_key=True, on_delete=models.CASCADE)
     username = models.CharField(max_length = 30, unique=True, null=False)
     telephone = models.BigIntegerField(null=False)
     country_code = models.IntegerField(null=False)
     dob = models.DateField()
     created_at = models.DateTimeField(auto_now_add = True)
     
'''
Describes the address of the user
Relation:
     M->O => user.UserProfile
'''   
class Address(models.Model):
     address_id = models.BigAutoField(primary_key=True)
     
     country = models.CharField(max_length=55)
     postcode = models.IntegerField()
     state_province = models.CharField(max_length=55)
     city = models.CharField(max_length=55)
     line_1 =  models.TextField()
     line_2 = models.TextField()
     line_3 = models.TextField()
     
     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
     
     
     
     
