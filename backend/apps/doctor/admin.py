from django.contrib import admin

from .models import AvailabilitySchedule, DoctorDetails, DoctorPatientAssignment

admin.site.register(DoctorDetails)
admin.site.register(AvailabilitySchedule)
admin.site.register(DoctorPatientAssignment)
