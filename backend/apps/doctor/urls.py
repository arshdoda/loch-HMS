from django.urls import path

from .views import *

urlpatterns = [
    path("create", DoctorCreateAPIView.as_view()),
    path("list", DoctorListAPIView.as_view()),
    path("availability/create", AvailabilityCreateAPIView.as_view()),
    path("availability/list", AvailabilityListAPIView.as_view()),
    path("assign/create", AssignPatientCreateAPIView.as_view()),
    path("assign/list", AssignPatientListAPIView.as_view()),
]
