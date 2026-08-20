from django.db import models

class Gender(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"

class GradeLevel(models.TextChoices):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"
    P6 = "P6"
    M1 = "M1"
    M2 = "M2"
    M3 = "M3"
    M4 = "M4"
    M5 = "M5"
    M6 = "M6"

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=64)
    school_code = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["name", "-created_at"],
                name="idx_school_name_created_at"
            ),
        ]

    def __str__(self):
        return self.name

class Classroom(models.Model):
    grade_level = models.CharField(
        max_length=16,
        choices=GradeLevel.choices,
    )
    room_no = models.CharField(max_length=16)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="classrooms",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(
                fields=["school", "grade_level", "room_no"],
                name="idx_classroom_school_grade",
            ),
        ]

    def __str__(self):
        return f"{self.grade_level}/{self.room_no}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(
        max_length=16,
        choices=Gender.choices,
    )
    classrooms = models.ManyToManyField(
        Classroom,
        related_name="teachers",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(
                fields=["first_name", "last_name"],
                name="idx_teacher_first_last__name",
            ),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    student_code = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(
        max_length=16,
        choices=Gender.choices,
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name="students",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["student_code"]
        indexes = [
            models.Index(
                fields=["first_name", "last_name"],
                name="idx_student_first_last_name",
            ),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"