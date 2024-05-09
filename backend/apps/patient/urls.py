from django.urls import path

from .views import *

urlpatterns = [
    path("create", PatientCreateAPIView.as_view()),
    path("list", PatientListAPIView.as_view()),
    path("appointment-record/create", AppointmentRecordCreateAPIView.as_view()),
    path("appointment-record/list", AppointmentRecordListAPIView.as_view()),
    path("medical-history/create", MedicalHistoryCreateAPIView.as_view()),
]
