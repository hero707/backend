from django.urls import path
from .views import login
from .views import authenticate
from .views import logout
from .views import token
urlpatterns = [
    path('login/', login),
    path('authenticate/', authenticate),
    path('logout/', logout),
    path('token/', token),
]
