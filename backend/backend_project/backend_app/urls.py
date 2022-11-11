from django.urls import re_path, path
from .views import GetAllUsers, CreateUser, GetUser

urlpatterns = [
  path('getallusers/', GetAllUsers),
  path('createuser/', CreateUser),
  re_path(r'^getuser/(?P<userid>[0-9]+)', GetUser)
  # re_path(r"^(?P<api_name>[a-z]+)", ListView, name='hotel-objects'),
]