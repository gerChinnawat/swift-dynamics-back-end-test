from rest_framework import serializers

from apis.models import Classroom, School, Student, Teacher


# School
class SchoolReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "id",
            "name",
            "school_code",
            "address",
            "is_active",
            "created_at",
            "updated_at",
        ]


class SchoolWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "name",
            "school_code",
            "address",
            "is_active",
        ]


# Classroom
class ClassroomReadSerializer(serializers.ModelSerializer):
    school = SchoolReadSerializer()

    class Meta:
        model = Classroom
        fields = [
            "id",
            "grade_level",
            "room_no",
            "school",
            "is_active",
            "created_at",
            "updated_at",
        ]


class ClassroomWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            "grade_level",
            "room_no",
            "school",
            "is_active",
        ]


# Teacher
class TeacherReadSerializer(serializers.ModelSerializer):
    classrooms = ClassroomReadSerializer(many=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "first_name",
            "last_name",
            "gender",
            "classrooms",
            "is_active",
            "created_at",
            "updated_at",
        ]


class TeacherWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "gender",
            "classrooms",
            "is_active",
        ]


# Student
class StudentReadSerializer(serializers.ModelSerializer):
    classroom = ClassroomReadSerializer()

    class Meta:
        model = Student
        fields = [
            "id",
            "student_code",
            "first_name",
            "last_name",
            "gender",
            "classroom",
            "is_active",
            "created_at",
            "updated_at",
        ]


class StudentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "student_code",
            "first_name",
            "last_name",
            "gender",
            "classroom",
            "is_active",
        ]
