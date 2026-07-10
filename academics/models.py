from django.db import models
from common.models import CommonAll
from centers.models import Branch
from employees.models import Employee

# Create your models here.
class Course(CommonAll):
    LANGUAGE_CHOICES = (
        ('uzb', 'Uzbek'),
        ('eng', 'English'),
        ('rus', 'Russian'),
    )
    title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES)
    certificate_available = models.BooleanField()

    def __str__(self):
        return self.title

class Group(CommonAll):
    title = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="groups")
    teacher = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="teaching_groups")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")

    def __str__(self):
        return self.title