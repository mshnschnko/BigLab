from django.shortcuts import render
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from collections import namedtuple

nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "user"  : nt(Users, UsersSerializer),
    "task"  : nt(Tasks, TasksSerializer),
    "message"   : nt(Messages, MessagesSerializer),
    "studentteacher": nt(StudentTeacher, StudentTeacherSerializer),
    "profiletype": nt(ProfileTypes, ProfileTypeSerializer),
}

@api_view(["GET"])
def GetAllUsers(request):
    object =  pattern.get("user", None)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers  = object.serializers(object_list, many=True)
        return Response(serializers.data)

@api_view(["GET"])
def GetUser(request, userid):
    object =  pattern.get("user", None)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.filter(id=userid)
        serializers  = object.serializers(object_list, many=True)
        return Response(serializers.data)

@api_view(["POST"])
def CreateUser(request):
    object =  pattern.get("user", None)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "POST":
        data = request.data
        print(data)
        serializers = object.serializers(data=data)
        
        if not serializers.is_valid():
            return Response(
                data   = serializers.error,
                status = status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
                #data   = serializers.error,
                status = status.HTTP_201_CREATED
        )