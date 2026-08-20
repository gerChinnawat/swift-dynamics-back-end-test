from rest_framework import viewsets

from apis.models import School
from apis.serializers import SchoolReadSerializer, SchoolWriteSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    filterset_fields = ["is_active"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SchoolReadSerializer
        return SchoolWriteSerializer
