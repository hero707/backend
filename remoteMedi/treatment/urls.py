from django.urls import path
from .views import createroom
from .views import patientWaitingList

urlpatterns = [
    path('createroom/', createroom),
    path('waitingroom/', patientWaitingList)
]
