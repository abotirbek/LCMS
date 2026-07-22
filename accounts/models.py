from django.contrib.auth.models import AbstractUser
from django.db import models

class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    telegram_username = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.phone_number

class Specialization(TimeStamped):
    name = models.CharField(max_length=50, help_text='e.g. English Teacher')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Department(TimeStamped):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Teacher(TimeStamped):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='specialization')
    experience = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (teacher)"


class Employee(TimeStamped):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='employee')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    experience = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (employee)"


class Student(TimeStamped):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student')
    parent_contact = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (student)"