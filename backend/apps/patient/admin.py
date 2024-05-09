from django.contrib import admin

from .models import AppointmentRecords, MedicalHistory, PatientDetails

admin.site.register(AppointmentRecords)
admin.site.register(MedicalHistory)
admin.site.register(PatientDetails)
