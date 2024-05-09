from apps.patient.models import PatientDetails
from common.enum import GENDER_CHOICES
from django.db import models
from django.utils import timezone

SPECIALIZATION_CHOICES = [
    ("general", "General"),
    ("orthopedics", "Orthopedics"),
    ("dermatology", "Dermatology"),
    ("radiology", "Radiology"),
]


class DoctorDetails(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    specialization = models.CharField(
        max_length=12, choices=SPECIALIZATION_CHOICES, db_index=True
    )
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{str(self.name)} | {self.get_specialization_display()}"


class AvailabilitySchedule(models.Model):
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, db_index=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{str(self.doctor.name)} | {self.doctor.get_specialization_display()}"


class DoctorPatientAssignment(models.Model):
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, db_index=True)
