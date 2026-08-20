from rest_framework import viewsets

from apis.filters import SchoolFilter
from apis.models import School
from apis.serializers import (
    SchoolDetailSerializer,
    SchoolWriteSerializer,
)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    filterset_class = SchoolFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SchoolDetailSerializer
        return SchoolWriteSerializer
