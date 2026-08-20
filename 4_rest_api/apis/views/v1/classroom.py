from rest_framework import viewsets

from apis.filters import ClassroomFilter
from apis.models import Classroom
from apis.serializers import ClassroomReadSerializer, ClassroomWriteSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.select_related("school").all()
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ClassroomReadSerializer
        return ClassroomWriteSerializer
