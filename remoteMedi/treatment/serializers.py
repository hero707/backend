from rest_framework import serializers
from .models import *
from django.http import JsonResponse, HttpResponse
from patient.serializers import PatientSerializer
class WaitingRoomSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model = WaitingRoom
        fields = ('room_number', 'patient', 'created_at')

    def validate(self, data):
        pass

    def save(self, **kwargs):
        pass

    def create(self, validated_data):
        pass
    
    def get_serializer_class(self):
        return WaitingRoomSerializer