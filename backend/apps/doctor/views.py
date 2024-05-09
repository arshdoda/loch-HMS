from common.custom_response import custom_error_response, custom_success_response
from common.pagination import SmallResultsSetPagination
from common.validations import date_validation
from rest_framework import generics, status

from .models import AvailabilitySchedule, DoctorDetails, DoctorPatientAssignment
from .serializers import (
    AssignPatientCreateSerializer,
    AssignPatientListSerializer,
    AvailabilityCreateSerializer,
    AvailabilityListSerializer,
    DoctorCreateSerializer,
    DoctorListSerializer,
)


class DoctorCreateAPIView(generics.CreateAPIView):
    serializer_class = DoctorCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Doctor Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Doctor Creation Failed", message=serializer.errors
            )


class AvailabilityCreateAPIView(generics.CreateAPIView):
    serializer_class = AvailabilityCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Availability Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Availability Creation Failed", message=serializer.errors
            )


class AssignPatientCreateAPIView(generics.CreateAPIView):
    serializer_class = AssignPatientCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Patient Assigned", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Patient Assignment Failed", message=serializer.errors
            )


class DoctorListAPIView(generics.GenericAPIView):
    serializer_class = DoctorListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        name = self.request.GET.get("name", None)
        gender = self.request.GET.get("gender", None)
        specialization = self.request.GET.get("specialization", None)
        filters = {}
        if name:
            filters["name"] = name
        if gender:
            filters["gender"] = gender.lower()
        if specialization:
            filters["specialization"] = specialization.lower()
        if filters:
            qs = DoctorDetails.objects.filter(**filters)
        else:
            qs = DoctorDetails.objects.all()

        return qs.order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        serializer = self.get_serializer(paginated_qs, many=True)
        return self.get_paginated_response(serializer.data)


class AvailabilityListAPIView(generics.GenericAPIView):
    serializer_class = AvailabilityListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        doctor = self.request.GET.get("doctor", None)
        date = self.request.GET.get("date", None)
        filters = {}
        if doctor:
            filters["doctor__name"] = doctor
        if date:
            filters["date"] = date_validation(date)
        if filters:
            qs = AvailabilitySchedule.objects.filter(**filters)
        else:
            qs = AvailabilitySchedule.objects.all()

        return qs.select_related("doctor").order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        serializer = self.get_serializer(paginated_qs, many=True)
        return self.get_paginated_response(serializer.data)


class AssignPatientListAPIView(generics.GenericAPIView):
    serializer_class = AssignPatientListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        doctor = self.request.GET.get("doctor", None)
        date = self.request.GET.get("date", None)
        filters = {}
        if doctor:
            filters["doctor__name"] = doctor
        if date:
            filters["date"] = date_validation(date)
        if filters:
            qs = DoctorPatientAssignment.objects.filter(**filters)
        else:
            qs = DoctorPatientAssignment.objects.all()

        return qs.order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        serializer = self.get_serializer(paginated_qs, many=True)
        return self.get_paginated_response(serializer.data)
