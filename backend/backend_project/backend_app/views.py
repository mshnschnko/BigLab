from django.shortcuts import render
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from collections import namedtuple
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "user"  : nt(Users, UsersSerializer),
    "task"  : nt(Tasks, TasksSerializer),
    "message"   : nt(Messages, MessagesSerializer),
    "studentteacher": nt(StudentTeacher, StudentTeacherSerializer),
    "profiletype": nt(ProfileTypes, ProfileTypeSerializer),
}

@api_view(["GET", "POST"])
def ProfileTypesRequest(request):
    typeid = request.GET.get("typeid", -1)
    object =  pattern.get("profiletype", None)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.filter(id=typeid) if typeid != -1 else object.model.objects.all()
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
def GetUser(request):
    object =  pattern.get("user", None)
    userid = request.GET.get("id", -1)
    userEmail = request.GET.get("email", "")
    # Users.objects.all().delete()
    if object == None or (userid == -1 and userEmail == ""):
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        if userid != -1:
            object_list = object.model.objects.filter(id=userid)
        if userEmail != "":
            object_list = object.model.objects.filter(email=userEmail)
        serializers  = object.serializers(object_list, many=True)
        if len(serializers.data) == 0:
            return Response(
                data   = "Invalid URL",
                status = status.HTTP_404_NOT_FOUND,
            )
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

@api_view(["GET"])
def CheckUser(request):
    object =  pattern.get("user", None)
    userid = request.GET.get("id", -1)
    userEmail = request.GET.get("email", "")
    userPassword = request.GET.get("password", "")
    # Users.objects.all().delete()
    if object == None or ((userid == -1 or userEmail == "") and userPassword == ""):
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        if userid != -1:
            object_list = object.model.objects.filter(id=userid)
        if userEmail != "":
            object_list = object.model.objects.filter(email=userEmail)
        serializers  = object.serializers(object_list, many=True)
        if len(serializers.data) == 0:
            return Response(
                data   = "Invalid email or password",
                status = status.HTTP_404_NOT_FOUND,
            )
        ret_data = {}
        for user in serializers.data:
            userAuth = authenticate(username=user['username'], password=userPassword)
            if not userAuth is None:
                ret_data = {'id': user['id'],
                                'name': user['name'],
                                'email': user['email'],
                                'profile_type': user['profile_type']}
            else:
                return Response(
                    data   = "Invalid email or password",
                    status = status.HTTP_404_NOT_FOUND,
                )
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
    else:
        return Response(
                data   = "Invalid URL",
                status = status.HTTP_404_NOT_FOUND,
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
        
        if not serializers.is_valid(raise_exception=True):
            return Response(
                data   = "Users with this email already exists",
                status = status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
                #data   = serializers.error,
                status = status.HTTP_201_CREATED
        )

@api_view(["GET", "POST"])
def Tasks(request):
    object =  pattern.get("task", None)
    taskid = request.GET.get("taskid", -1)
    # Users.objects.all().delete()
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.filter(id=taskid) if taskid != -1 else object.model.objects.all()
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