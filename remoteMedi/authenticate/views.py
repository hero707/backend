from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
import json

@api_view(['POST'])
def login(request):

    body_data = json.loads(request.body)
    print(body_data)

    data = json.dumps(body_data)

    response = requests.post(url = settings.AUTH_SERVER_LOGIN, data=data, headers = {"content-type": "application/json"} )
    print(json.loads(response.content))


    return Response(json.loads(response.content), status=response.status_code)


@api_view(['GET'])
def authenticate(request):
    requests.get(url = settings.AUTH_SERVER_AUTHENTICATE, headers = request.headers)
    
    return Response()