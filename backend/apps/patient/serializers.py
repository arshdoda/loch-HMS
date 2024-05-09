from rest_framework import serializers

from .models import AppointmentRecords, MedicalHistory, PatientDetails


class PatientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientDetails
        fields = "__all__"


class MedicalHistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalHistory
        fields = "__all__"


class AppointmentRecordsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentRecords
        fields = "__all__"


class MedicalHistoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalHistory
        exclude = ["id", "patient"]


class PatientListSerializer(serializers.ModelSerializer):
    medical_history = MedicalHistoryListSerializer(read_only=True)
    gender = serializers.SerializerMethodField()

    def get_gender(self, instance):
        return instance.get_gender_display()

    class Meta:
        model = PatientDetails
        fields = ["id", "name", "gender", "age", "phone_number", "medical_history"]


class AppointmentRecordListSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    def get_patient_name(self, instance):
        return instance.patient.name

    class Meta:
        model = AppointmentRecords
        exclude = ["id", "patient"]
