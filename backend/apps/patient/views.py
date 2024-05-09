from common.custom_response import custom_error_response, custom_success_response
from common.pagination import SmallResultsSetPagination
from common.validations import date_validation
from rest_framework import generics, status

from .models import AppointmentRecords, PatientDetails
from .serializers import (
    AppointmentRecordListSerializer,
    AppointmentRecordsCreateSerializer,
    MedicalHistoryCreateSerializer,
    PatientCreateSerializer,
    PatientListSerializer,
)


class AppointmentRecordCreateAPIView(generics.GenericAPIView):
    serializer_class = AppointmentRecordsCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Appointment Record Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Appointment Record Failed", message=serializer.errors
            )


class PatientCreateAPIView(generics.GenericAPIView):
    serializer_class = PatientCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Patient Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Patient Creation Failed", message=serializer.errors
            )


class MedicalHistoryCreateAPIView(generics.GenericAPIView):
    serializer_class = MedicalHistoryCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Medical History Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Medical History Creation Failed", message=serializer.errors
            )


class PatientListAPIView(generics.GenericAPIView):
    serializer_class = PatientListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        name = self.request.GET.get("name", None)
        gender = self.request.GET.get("gender", None)
        filters = {}
        if name:
            filters["name"] = name
        if gender:
            filters["gender"] = gender.lower()
        if filters:
            qs = PatientDetails.objects.filter(**filters)
        else:
            qs = PatientDetails.objects.all()

        return qs.select_related("medical_history").order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        serializer = self.get_serializer(paginated_qs, many=True)
        return self.get_paginated_response(serializer.data)


class AppointmentRecordListAPIView(generics.GenericAPIView):
    serializer_class = AppointmentRecordListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        patient = self.request.GET.get("patient", None)
        date = self.request.GET.get("date", None)
        filters = {}
        if patient:
            filters["patient__name"] = patient
        if date:
            filters["appointment_date"] = date_validation(date)
        if filters:
            qs = AppointmentRecords.objects.filter(**filters)
        else:
            qs = AppointmentRecords.objects.all()

        return qs.select_related("patient").order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        serializer = self.get_serializer(paginated_qs, many=True)
        return self.get_paginated_response(serializer.data)
