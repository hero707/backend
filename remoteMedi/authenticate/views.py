from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
import json


@api_view(['POST'])
def login(request):

    try:
        body_data = json.loads(request.body)
        print(body_data) # 값 리턴 

    except Exception as e:
        pass

    response = requests.post(settings.AUTH_SERVER_LOGIN, data=body_data)
    print(response)
    content = {'please move along': 'nothing to see here'}
    return Response(content, status=response.status_code)