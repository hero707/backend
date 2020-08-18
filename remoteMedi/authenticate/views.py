from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def login(request):
    # authServer로 요청 보내기!

    # Serialize로 리턴 데이터 만들기

    # 리턴
    return Response(status=status.HTTP_200_OK)
