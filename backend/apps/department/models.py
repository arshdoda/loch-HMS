from apps.doctor.models import DoctorDetails
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    doctors = models.ManyToManyField(DoctorDetails, related_name="departments")

    def __str__(self):
        return f"{str(self.name)}"


class Services(models.Model):
    service = models.CharField(max_length=20, db_index=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="services"
    )

    def __str__(self):
        return f"{str(self.service)}"
