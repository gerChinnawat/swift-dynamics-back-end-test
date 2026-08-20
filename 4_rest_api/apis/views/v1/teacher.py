from rest_framework import viewsets

from apis.filters import TeacherFilter
from apis.models import Teacher
from apis.serializers import TeacherReadSerializer, TeacherWriteSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.prefetch_related("classrooms").all()
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TeacherReadSerializer
        return TeacherWriteSerializer
