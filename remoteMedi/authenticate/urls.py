from django.urls import path
from .views import login
from .views import authenticate
urlpatterns = [
    path('login/', login),
    path('authenticate/', authenticate),
]
