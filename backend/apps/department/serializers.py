from rest_framework import serializers

from .models import Department, Services


class DepartmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class ServicesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = "__all__"


class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

    def to_representation(self, value):
        rep = super().to_representation(value)

        context_doc = self.context.get("doctors", {})
        doctors = [context_doc[i] for i in rep["doctors"]]
        rep["doctors"] = doctors

        context_services = self.context.get("services", {})
        if rep["id"] in context_services:
            rep["services"] = [i.service for i in context_services[rep["id"]]]
        else:
            rep["services"] = []
        return rep


class ServicesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        exclude = ["department"]
