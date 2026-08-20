from rest_framework import viewsets

from apis.filters import ClassroomFilter
from apis.models import Classroom
from apis.serializers import (
    ClassroomDetailSerializer,
    ClassroomReadSerializer,
    ClassroomWriteSerializer,
)


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.select_related("school").all()
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return ClassroomDetailSerializer
        return ClassroomWriteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "retrieve":
            queryset = queryset.prefetch_related("teachers", "students")
        return queryset
