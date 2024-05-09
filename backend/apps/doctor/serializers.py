from rest_framework import serializers

from .models import AvailabilitySchedule, DoctorDetails, DoctorPatientAssignment


class DoctorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorDetails
        fields = "__all__"


class AvailabilityCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailabilitySchedule
        fields = "__all__"


class AssignPatientCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that the doctor availability.
        """
        date = data.get("date", None)
        is_available = AvailabilitySchedule.objects.filter(date=date).exists()
        if not is_available:
            raise serializers.ValidationError(
                "Doctor is not available on the given date"
            )
        return data

    class Meta:
        model = DoctorPatientAssignment
        fields = "__all__"


class DoctorListSerializer(serializers.ModelSerializer):
    specialization = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    def get_gender(self, instance):
        return instance.get_gender_display()

    def get_specialization(self, instance):
        return instance.get_specialization_display()

    class Meta:
        model = DoctorDetails
        fields = "__all__"


class AvailabilityListSerializer(serializers.ModelSerializer):
    doctor = serializers.ReadOnlyField(source="doctor.name")

    class Meta:
        model = AvailabilitySchedule
        fields = "__all__"


class AssignPatientListSerializer(serializers.ModelSerializer):
    doctor = serializers.ReadOnlyField(source="doctor.name")
    patient = serializers.ReadOnlyField(source="patient.name")

    class Meta:
        model = DoctorPatientAssignment
        fields = "__all__"
