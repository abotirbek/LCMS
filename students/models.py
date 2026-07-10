from django.db import models
from django.db.models.functions import Now
from common.models import CommonAll, CommonIndividuals
from academics.models import Group

# Create your models here.
class Student(CommonAll, CommonIndividuals):
    enrollment_date = models.DateField()
    parent_contact = models.CharField(max_length=16)
    address = models.TextField()

    def __str__(self):
        return self.name

class Enrollment(CommonAll):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="enrollments")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(default=Now())
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.name} -> {self.group.title}"

class Attendance(CommonAll):
    ATTENDANCE_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="attendance_records")
    lesson_date = models.DateField()
    status = models.CharField(max_length=7, choices=ATTENDANCE_CHOICES)

    def __str__(self):
        return str(self.id)