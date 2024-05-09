from common.enum import GENDER_CHOICES
from django.db import models


class PatientDetails(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{str(self.name)}"


class MedicalHistory(models.Model):
    patient = models.OneToOneField(
        PatientDetails, on_delete=models.CASCADE, related_name="medical_history"
    )
    previous_diagnoses = models.TextField()
    allergies = models.TextField()
    medications = models.TextField()

    def __str__(self):
        return f"{str(self.patient.name)}"


class AppointmentRecords(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{str(self.patient.name)}"
