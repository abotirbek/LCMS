from django.db import models
from centers.models import Branch
from accounts.models import Teacher, Student, TimeStamped


# Create your models here.
class Course(TimeStamped):
    LANGUAGE_CHOICES = (
        ('uzb', 'Uzbek'),
        ('eng', 'English'),
        ('rus', 'Russian'),
    )
    title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES)
    has_certificate = models.BooleanField()

    def __str__(self):
        return self.title

class Groups(TimeStamped):
    title = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    students = models.ManyToManyField(Student, related_name='student_group', null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_group")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="branch")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")

    def __str__(self):
        return self.title

class Module(TimeStamped):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_module')
    description = models.TextField()
    files = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title

class RoomType(TimeStamped):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Room(TimeStamped):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="room_type")
    has_projector = models.BooleanField()
    has_desk = models.BooleanField()
    floor = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="branch_room")

    def __str__(self):
        return self.name

class Lesson(TimeStamped):
    start_time = models.TimeField()
    stop_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.room.name