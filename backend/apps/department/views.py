import itertools

from apps.doctor.models import DoctorDetails
from common.custom_response import custom_error_response, custom_success_response
from common.pagination import SmallResultsSetPagination
from rest_framework import generics, status

from .models import Department, Services
from .serializers import (
    DepartmentCreateSerializer,
    DepartmentListSerializer,
    ServicesCreateSerializer,
    ServicesListSerializer,
)


class DepartmentCreateAPIView(generics.CreateAPIView):
    serializer_class = DepartmentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Department Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Department Creation Failed", message=serializer.errors
            )


class ServicesCreateAPIView(generics.CreateAPIView):
    serializer_class = ServicesCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return custom_success_response(
                message="Service Created", status=status.HTTP_201_CREATED
            )
        else:
            return custom_error_response(
                error="Service Creation Failed", message=serializer.errors
            )


class DepartmentListAPIView(generics.GenericAPIView):
    serializer_class = DepartmentListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        name = self.request.GET.get("name", None)
        doctor = self.request.GET.get("doctor", None)
        service = self.request.GET.get("service", None)
        filters = {}
        if name:
            filters["name"] = name
        if doctor:
            filters["doctors__name"] = doctor
        if service:
            filters["services__service"] = service
        if filters:
            qs = Department.objects.filter(**filters)
        else:
            qs = Department.objects.all()

        return qs.prefetch_related("doctors").order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        id_list = []
        for dep in paginated_qs:
            for doc in dep.doctors.all():
                id_list.append(doc.id)
        obj = DoctorDetails.objects.filter(id__in=set(id_list)).only("id", "name")
        doctors = {o.id: o.name for o in obj}

        dep_services = Services.objects.filter(department__in=paginated_qs).only(
            "department_id", "service"
        )
        sorted_service = sorted(dep_services, key=lambda x: (x.department_id))
        grouped_services = {
            key: list(group)
            for key, group in itertools.groupby(
                sorted_service, lambda x: x.department_id
            )
        }

        serializer = self.get_serializer(
            paginated_qs,
            many=True,
            context={"doctors": doctors, "services": grouped_services},
        )
        return self.get_paginated_response(serializer.data)


class ServicesListAPIView(generics.GenericAPIView):
    serializer_class = ServicesListSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        service = self.request.GET.get("service", None)
        filters = {}
        if service:
            filters["service"] = service
        if filters:
            qs = Services.objects.filter(**filters)
        else:
            qs = Services.objects.all()

        return qs.order_by("id")

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_qs = self.paginate_queryset(qs)
        serializer = self.get_serializer(paginated_qs, many=True)
        return self.get_paginated_response(serializer.data)
