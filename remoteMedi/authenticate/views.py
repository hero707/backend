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
        print(body_data)
    except Exception as e:
        pass

    #response = requests.POST('http://example.com')
       
    content = {'please move along': 'nothing to see here'}
    return Response(content, status=status.HTTP_200_OK)