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

@api_view(["GET", "POST"])
def ProfileTypesRequest(request, typeid):
    object =  pattern.get("profiletype", None)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.filter(id=typeid) if typeid != "" else object.model.objects.all()
        serializers  = object.serializers(object_list, many=True)
        print(serializers.data)
        return Response(serializers.data)

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

# @api_view(["GET"])
# def GetAllUsers(request):
#     object =  pattern.get("user", None)
#     # Users.objects.all().delete()
#     if object == None:
#         return Response(
#             data   = "Invalid URL",
#             status = status.HTTP_404_NOT_FOUND,
#         )
#     if request.method == "GET":
#         object_list = object.model.objects.all()
#         serializers  = object.serializers(object_list, many=True)
#         return Response(serializers.data)

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
        object_list = object.model.objects.filter(id=userid) if userid != "" else object.model.objects.all()
        serializers  = object.serializers(object_list, many=True)
        print(serializers.data[0]['name'])
        ret_data = []
        for user in serializers.data:
            ret_data.append({'id': user['id'],
                            'name': user['name'],
                            'email': user['email'],
                            'profile_type': user['profile_type']})
        return Response(
            data = ret_data,
            # data={
            #     'id': serializers.data[0]['id'],
            #     'name': serializers.data[0]['name'],
            #     'email': serializers.data[0]['email'],
            #     'profile_type': serializers.data[0]['profile_type']
            #     },
            status = status.HTTP_200_OK) if serializers.data != [] else Response(
                                                                            data = "There is no user with this ID",
                                                                            status=status.HTTP_404_NOT_FOUND
                                                                        )

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
                data   = "User with this email already exists",
                status = status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
                #data   = serializers.error,
                status = status.HTTP_201_CREATED
        )

@api_view(["GET", "POST"])
def Tasks(request, taskid):
    object =  pattern.get("task", None)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.filter(id=taskid) if taskid != "" else object.model.objects.all()
        serializers  = object.serializers(object_list, many=True)
        print(serializers.data)
        return Response(serializers.data) if serializers.data != [] else Response(data = "There is no task with this ID", status=status.HTTP_404_NOT_FOUND)

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