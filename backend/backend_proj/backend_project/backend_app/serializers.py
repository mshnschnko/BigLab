from rest_framework import fields, serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

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
        model = Student_Teacher
        fields = "__all__"