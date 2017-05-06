from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError

from rest_api.serializers import UserSerializer
#from core.models import BaseUser, Friend, Feed, Reply, Picture


# This function is needed to support POST with JSON in firefox.
def options_cors():
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = 1000
    # note that '*' is not valid for Access-Control-Allow-Headers
    response['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
    return response

# may only admin can access
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes =

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_login(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        username = request.data.get('id', None)
        password = request.data.get('password', None)
        if username is None:
            return Response({'message':'Please put valid ID.'}, status=400)
        if password is None:
            return Response({'message':'Please put password.'}, status=400)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400) #sets the exp. value of the session
                login(request, user) #the user is now logged in
                return Response('',status=200)
            return Response({'message': 'User is not active.'}, status=403)
        else:
            return Response({'message': 'Invalid ID and password.'},status=400)
    
    def options(self, request):
        return options_cors()

class user_signup(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        username = request.data.get('id', None)
        password = request.data.get('password', None)
        if username is None:
            return Response({'message':'Please put valid ID.'}, status=400)
        if password is None:
            return Response({'message':'Please put password.'}, status=400)
        
        try:
            user = User.objects.create_user(username, 'default@email.com', password)
        except IntegrityError:
            return Response({'message':'User already exists!'}, status=400)
        user.save()
        return Response('',status=200)
    
    def options(self, request):
        return options_cors()
