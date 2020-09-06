from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Visit
from django.db.models import F
import datetime
# Create your views here.


@api_view(['GET'])
def visit(request):
    visit, created = Visit.objects.get_or_create(
            created_at=datetime.date.today()
        )

    if created:
        return Response({'response' : 'good day! you are the first person today'}, status=200)
    
    Visit.objects.filter(id=visit.id).update(visit = F('visit') + 1)
    return Response({'response' : f'today visit : {visit.visit + 1}'}, status=200)

