from rest_framework import fields, serializers
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.contrib.auth.hashers import make_password
from .models import *

class ProfileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileTypes
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

    error = "ERROR"

    def create(self, validated_data):
        # Using validated_data dict as kwargs for create_user
        return Users.objects.create_user(**validated_data)


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"

class StudentTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTeacher
        fields = "__all__"

    error = "ERROR"