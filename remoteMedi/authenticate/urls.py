from django.urls import path
from .views import login
from .views import authenticate
from .views import logout
urlpatterns = [
    path('login/', login),
    path('authenticate/', authenticate),
]
