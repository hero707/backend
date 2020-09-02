from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
import json

@api_view(['POST'])
def login(request):
    response = requests.post(url = settings.AUTH_SERVER_LOGIN, data=request.body, headers = {"content-type": "application/json"} )
    return Response(json.loads(response.content), status=response.status_code)


@api_view(['GET'])
def authenticate(request):
    requests.get(url = settings.AUTH_SERVER_AUTHENTICATE, headers = request.headers)    
    return Response()


@api_view(['DELETE'])
def logout(request):
    requests.delete(url = settings.AUTH_SERVER_LOGOUT, data = request.body, headers = {"content-type": "application/json"} )    
    return Response() 


@api_view(['POST'])
def token(request):
    response = requests.post(url = settings.AUTH_SERVER_TOKEN, data = request.body, headers = {"content-type": "application/json"} )    
    return Response(response.content), status=response.status_code)