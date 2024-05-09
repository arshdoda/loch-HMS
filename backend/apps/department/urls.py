from django.urls import path

from .views import *

urlpatterns = [
    path("create", DepartmentCreateAPIView.as_view()),
    path("list", DepartmentListAPIView.as_view()),
    path("services/create", ServicesCreateAPIView.as_view()),
    path("services/list", ServicesListAPIView.as_view()),
]
