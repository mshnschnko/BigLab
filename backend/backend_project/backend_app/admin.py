from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Messages)
admin.site.register(Tasks)
admin.site.register(StudentTeacher)
admin.site.register(ProfileTypes)