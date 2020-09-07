from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import redirect
import requests
from django.conf import settings
import json

# Create your views here.



@api_view(['GET'])
def kakaologin(request):
    client_id = settings.KAKAO_API
    redirect_uri = f"{settings.HOST}/authenticate/kakao/auth"

    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

def kakaoauth(request):
    code = request.GET['code']
    client_id = settings.KAKAO_API
    redirect_uri = f"{settings.HOST}/authenticate/kakao/auth"
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    client_secret = settings.KAKAO_SECRET

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code
    access_token_request_uri += "&client_secret=" + client_secret

    print(access_token_request_uri)
    token_request = requests.get(access_token_request_uri)

    return JsonResponse(token_request.json(), status=200)
    
    

@api_view(['POST'])
def kakaologout(request):
    client_id = settings.KAKAO_API
    Authorization = json.loads(request.body)

    print(Authorization)
    logout_url = "https://kapi.kakao.com/v1/user/logout"

    
    logout_id = requests.post(url=logout_url, headers = Authorization)
    print(json.loads(logout_id.content))
    return Response(json.loads(logout_id.content) , status=logout_id.status_code)