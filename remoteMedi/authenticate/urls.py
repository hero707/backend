from django.urls import path
from .views import kakaologin
from .views import kakaoauth
from .views import kakaologout


urlpatterns = [
    path('kakao/auth/', kakaoauth),
    path('kakao/login/', kakaologin),
    path('kakao/logout/', kakaologout),
]
