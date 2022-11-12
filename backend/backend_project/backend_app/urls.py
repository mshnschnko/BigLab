from django.urls import re_path, path
from .views import CreateUser, GetUser, ProfileTypesRequest, Tasks

urlpatterns = [
  # path('getallusers/', GetAllUsers),
  path('register/', CreateUser),
  re_path(r'^profiletypes/(?P<typeid>[0-9]*)', ProfileTypesRequest),
  re_path(r'^task/(?P<taskid>[0-9]*)', Tasks),
  re_path(r'^getuser/(?P<userid>[0-9]*)', GetUser),
  # re_path(r"^(?P<api_name>[a-z]+)", ListView, name='hotel-objects'),
]