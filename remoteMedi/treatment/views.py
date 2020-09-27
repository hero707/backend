from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WaitingRoom
from .models import Patient
from .models import Major
from rest_framework import status
from django.core import serializers
import json
import hashlib
from .serializers import WaitingRoomSerializer
# Create your views here.


@api_view(['POST'])
def createroom(request):
    res = json.loads(request.body)
   
    
    enc = hashlib.md5()
    enc.update(res['Patient'].encode('utf-8'))
    encText = enc.hexdigest()

    patient = Patient.objects.get(name=res['Patient'])
    major = Major.objects.get(name=res['Major'])

    fb = WaitingRoom(patient = patient, major = major, room_number=encText)
    fb.save()
    
    return Response(status=status.HTTP_200_OK)
    
@api_view(['GET'])
def patientWaitingList(request):
    res = request.GET.get('Major', None)
    major_instance = Major.objects.get(name=res)
    WaitingRoom_list = WaitingRoom.objects.filter(major=major_instance)
    #WaitingRoom_list_json = serializers.serialize('json', WaitingRoom_list)
    ser = WaitingRoomSerializer(data=WaitingRoom_list, many=True)
    if ser.is_valid():
        pass

    return Response(ser.data,status=status.HTTP_200_OK)

