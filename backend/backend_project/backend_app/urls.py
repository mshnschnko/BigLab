from django.urls import re_path, path
from .views import GetAllUsers, CreateUser, GetUser, ProfileTypesRequest

urlpatterns = [
  path('getallusers/', GetAllUsers),
  path('register/', CreateUser),
  path('profiletypes/', ProfileTypesRequest),
  re_path(r'^getuser/(?P<userid>[0-9]+)', GetUser)
  # re_path(r"^(?P<api_name>[a-z]+)", ListView, name='hotel-objects'),
]