# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from django.http import HttpResponse
from storybeta.serializers import StorySerializer,UserSerializer,IterationSerializer,CommentSerializer, UserExtrasSerializer
from storybeta.models import Story,UserExtras,Iterations,Comments
from rest_framework import status, generics
from rest_framework import viewsets



# Create your views here.
@csrf_exempt
def userlogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request,user)
        responce = {"status":"user logged in successfully","username": user.get_username(),"user_id": usr }
    else:
        responce = {"status":"user not authenticated"}
    return JsonResponse(responce)



# @api_view(['GET','POST'])
# def story_list(request):
#     if request.method == "GET":
#         story = Story.objects.all()
#         serializer = StorySerializer(story,many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = StorySerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status= status.HTTP_201_CREATED)
#         return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','POST'])
# def user_list(request):
#     if request.method == "GET":
#         user = User.objects.all()
#         serializer = UserSerializer(user,many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = UserSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status= status.HTTP_201_CREATED)
#         return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    
class UserExtraViewSet(viewsets.ModelViewSet):
    queryset = UserExtras.objects.all()
    serializer_class = UserExtrasSerializer


class IterationViewSet(viewsets.ModelViewSet):
    queryset = Iterations.objects.all()
    serializer_class = IterationSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

