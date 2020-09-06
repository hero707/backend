from django.urls import path
from .views import visit
urlpatterns = [
    path('visit/', visit),
]
