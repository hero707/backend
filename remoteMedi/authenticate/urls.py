from django.urls import path
from .views import login
from .views import kakaologin
from .views import kakaoauth
from .views import kakaologout
from .views import kakaosendmsg

urlpatterns = [
    path('login/', login),
    path('kakaoauth/', kakaoauth),
    path('kakaologin/', kakaologin),
    path('kakaologout/', kakaologout),
    path('kakaosendmsg/', kakaosendmsg),
]
