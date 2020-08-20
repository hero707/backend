from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import json

# Create your views here.


@api_view(['POST'])
def login(request):

    try:
        body_data = json.loads(request.body)
        print(body_data) # 값 리턴 

    except Exception as e:
        pass

    #response = requests.POST('127.0.0.1:4000/login') # body
    datas = body_data
    URL = 'http://127.0.0.1:4000/login'
    #res = requests.post(URL)
    response = requests.post(URL, data=datas)
    
    content = {'please move along': 'nothing to see here'}
    return Response(content, status=status.HTTP_200_OK)

    


@api_view(['POST'])
def logout(request):

    try:
        datas = json.loads(request.body)
        print(datas) # 값 리턴 

    except Exception as e:
        pass

    #response = requests.POST('127.0.0.1:4000/login') # body
    URL = 'http://127.0.0.1:4000/login'
    #res = requests.post(URL)
    response = requests.post(URL, data=datas)
    content = datas
    return Response(content, status=status.HTTP_200_OK)