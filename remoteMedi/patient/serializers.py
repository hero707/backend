from rest_framework import serializers
from .models import *
from django.http import JsonResponse, HttpResponse

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def validate(self, data):
        pass

    def save(self, **kwargs):
        pass

    def create(self, validated_data):
        pass
    
    def get_serializer_class(self):
        return PatientSerializer