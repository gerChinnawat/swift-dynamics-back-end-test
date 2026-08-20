from django_filters import FilterSet, filters

from apis.models import Classroom, Gender, GradeLevel, School, Student, Teacher


class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = School
        fields = ["name", "school_code", "is_active"]


class ClassroomFilter(FilterSet):
    grade_level = filters.ChoiceFilter(choices=GradeLevel.choices)

    class Meta:
        model = Classroom
        fields = ["school", "grade_level", "room_no", "is_active"]


class TeacherFilter(FilterSet):
    gender = filters.ChoiceFilter(choices=Gender.choices)
    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Teacher
        fields = ["gender", "first_name", "last_name", "classrooms", "is_active"]


class StudentFilter(FilterSet):
    gender = filters.ChoiceFilter(choices=Gender.choices)
    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")
    school = filters.NumberFilter(field_name="classroom__school_id")

    class Meta:
        model = Student
        fields = [
            "gender",
            "first_name",
            "last_name",
            "classroom",
            "school",
            "is_active",
        ]
