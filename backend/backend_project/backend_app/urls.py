from django.urls import re_path, path
from .views import CreateUser, GetUser, ProfileTypesRequest, Tasks, CheckUser, SubjectsRequest, StudentTeacherRequest

urlpatterns = [
  # path('getallusers/', GetAllUsers),
  path('register', CreateUser),
  path('profiletypes', ProfileTypesRequest),
  path('task', Tasks),
  path('user', GetUser),
  path('checkuser', CheckUser),
  path('subject', SubjectsRequest),
  path('pairs', StudentTeacherRequest),
  # path(r'^getuserbyemail/', GetUserByEmail)
  # re_path(r"^(?P<api_name>[a-z]+)", ListView, name='hotel-objects'),
]