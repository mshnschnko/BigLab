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
    "subject": nt(Subjects, SubjectSerializer),
}

@api_view(["GET", "POST"])
def ProfileTypesRequest(request):
    typeid = request.GET.get("typeid", -1)
    object =  pattern.get("profiletype", None)
    # Users.objects.all().delete()
    if object is None:
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
def GetUser(request):
    object =  pattern.get("user", None)
    getquery = request.GET.get("query", "")
    # Users.objects.all().delete()
    if object is None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        if getquery == "":
            return Response(
                data   = "Incorrect query params",
                status = status.HTTP_404_NOT_FOUND,
            )
        if getquery == "profile":
            expectedProfileType = request.GET.get("type", -1)
            if expectedProfileType == -1:
                return Response(
                    data   = "Incorrect profile type",
                    status = status.HTTP_404_NOT_FOUND,
                )
            object_list = object.model.objects.filter(profile_type=expectedProfileType)
        if getquery == "id":
            userid = request.GET.get("id", -1)
            if userid == -1:
                return Response(
                    data   = "Incorrect user's id",
                    status = status.HTTP_404_NOT_FOUND,
                )
            object_list = object.model.objects.filter(id=userid)
        if getquery == "email":
            userEmail = request.GET.get("email", "")
            if userEmail == "":
                return Response(
                    data   = "Incorrect user's email",
                    status = status.HTTP_404_NOT_FOUND,
                )
            object_list = object.model.objects.filter(email=userEmail)
        if getquery == "all":
            object_list = object.model.objects.all()
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
                            'profile_type': user['profile_type'],
                            'subject': user['subject']})
        # ret_data = {'id': serializers.data[0]['id'],
        #                     'name': serializers.data[0]['name'],
        #                     'email': serializers.data[0]['email'],
        #                     'profile_type': serializers.data[0]['profile_type']}
        # for user in serializers.data:
        #     ret_data.append({'id': user['id'],
        #                     'name': user['name'],
        #                     'email': user['email'],
        #                     'profile_type': user['profile_type']})
        # ret_data = {
        #         'id': serializers.data[0]['id'],
        #         'name': serializers.data[0]['name'],
        #         'email': serializers.data[0]['email'],
        #         'profile_type': serializers.data[0]['profile_type']
        #         }
        # if serializers.data[0]['profile_type'] == 3:
        #     ret_data['subject'] = serializers.data[0]['subject']
        # print(serializers.data[0]['profile_type'])
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
    if object is None or ((userid == -1 or userEmail == "") and userPassword == ""):
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
        # for user in serializers.data:
        userAuth = authenticate(username=serializers.data[0]['username'], password=userPassword)
        if not userAuth is None:
            ret_data = {'id': serializers.data[0]['id'],
                            'name': serializers.data[0]['name'],
                            'email': serializers.data[0]['email'],
                            'profile_type': serializers.data[0]['profile_type']}
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
    if object is None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "POST":
        data = request.data
        print(data)
        serializers = object.serializers(data=data)
        
        if not serializers.is_valid(raise_exception=True):
            print("already")
            return Response(
                data   = "Users with this email already exists",
                status = status.HTTP_409_CONFLICT
            )
        serializers.save()
        object_list = object.model.objects.filter(email=request.data['email'])
        serializers1  = object.serializers(object_list, many=True)
        return Response(
                data   = {'id': serializers1.data[0]['id'],
                            'name': serializers1.data[0]['name'],
                            'email': serializers1.data[0]['email'],
                            'profile_type': serializers1.data[0]['profile_type']},
                status = status.HTTP_201_CREATED
        )

@api_view(["GET", "POST", "PATCH"])
def Task(request):
    object =  pattern.get("task", None)
    queryparam = request.GET.get("query", "")
    # Users.objects.all().delete()
    if object is None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        if queryparam == "":
            return Response(
                data   = "Incorrect query params",
                status = status.HTTP_404_NOT_FOUND,
            )
        if queryparam == "all":
            object_list = object.model.objects.all()
        if queryparam == "byuserid":
            userid = request.GET.get("id", -1)
            if userid == -1:
                return Response(
                data   = "Incorrect user id",
                status = status.HTTP_404_NOT_FOUND,
            )
            relations = StudentTeacher.objects.filter(student_id = userid) | StudentTeacher.objects.filter(teacher_id = userid)
            serializers2 = pattern.get("studentteacher", None).serializers(relations, many=True)
            relationsids = []
            for item in serializers2.data:
                relationsids.append(item['id'])
            object_list = object.model.objects.filter(relation_id__in = relationsids)
        if queryparam == "bytaskid":
            taskid = request.GET.get("id", -1)
            if taskid == -1:
                return Response(
                data   = "Incorrect task id",
                status = status.HTTP_404_NOT_FOUND,
            )
            object_list = object.model.objects.filter(id = taskid)
        serializers  = object.serializers(object_list, many=True)
        print(serializers.data)
        return Response(
            data=serializers.data,
            status=status.HTTP_200_OK
        )

    if request.method == "POST":
        data = request.data
        #print(data)
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

    if request.method == "PATCH":
        data = request.data
        res = object.model.objects.filter(id = data['id']).update(task_status = data['new_status'], completion_time = data['completion_time'])
        return Response(
            status=status.HTTP_202_ACCEPTED
        )

@api_view(["GET", "POST"])
def SubjectsRequest(request):
    subjid = request.GET.get("subjid", -1)
    subj = request.GET.get("subjid", "")
    object =  pattern.get("subject", None)
    # Users.objects.all().delete()
    if object is None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        if  subjid == -1 and subj == "":
            object_list = object.model.objects.all()
        else:
            object_list = object.model.objects.filter(id=subjid) if subjid != -1 else object.model.objects.filter(subject=subj)
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

@api_view(["GET", "POST"])
def StudentTeacherRequest(request):
    studid = request.GET.get("studid", -1)
    tutorid = request.GET.get("tutorid", -1)
    object =  pattern.get("studentteacher", None)
    # Users.objects.all().delete()
    if object is None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        if  studid == -1 and tutorid == -1:
            object_list = object.model.objects.all()
        elif tutorid == -1:
            object_list = object.model.objects.filter(student_id=studid)
        elif studid == -1:
            object_list = object.model.objects.filter(teacher_id=tutorid)
        else:
            object_list = object.model.objects.filter(student_id=studid) & object.model.objects.filter(teacher_id=tutorid)
        serializers  = object.serializers(object_list, many=True)
        # print(serializers.data)
        return Response(serializers.data)

    if request.method == "POST":
        data = request.data
        users = Users.objects.filter(id = data['student_id']) | Users.objects.filter(id = data['teacher_id'])
        serializers2  = pattern.get("user", None).serializers(users, many=True)
        if not ((serializers2.data[0]['profile_type'] == 2 and serializers2.data[0]['id'] == int(data['student_id'])
                and serializers2.data[1]['profile_type'] == 3 and serializers2.data[1]['id'] == int(data['teacher_id'])) or
                (serializers2.data[1]['profile_type'] == 2 and serializers2.data[1]['id'] == int(data['student_id'])
                and serializers2.data[0]['profile_type'] == 3 and serializers2.data[0]['id'] == int(data['teacher_id']))):
                    return Response(
                        data   = "Incorrect profile types",
                        status = status.HTTP_404_NOT_FOUND
                    )
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