from django.urls import path
from . import views

urlpatterns = [
     path("p_auth/", view=views.PrimaryAuthView.as_view())
]