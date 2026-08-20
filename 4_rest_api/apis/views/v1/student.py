from rest_framework import viewsets

from apis.models import Student
from apis.serializers import StudentReadSerializer, StudentWriteSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("classroom").all()
    filterset_fields = ["classroom", "gender", "is_active"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentReadSerializer
        return StudentWriteSerializer
