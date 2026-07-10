from tkinter.scrolledtext import example

from django.db import models
from common.models import CommonAll, CommonIndividuals

# Create your models here.
class Department(CommonAll):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Specialization(CommonAll):
    name = models.CharField(max_length=50, help_text='e.g. English Teacher')

    def __str__(self):
        return self.name

class Employee(CommonAll, CommonIndividuals):
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualification = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name="specialization")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="department")

    def __str__(self):
        return self.name