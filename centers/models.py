from django.db import models
from common.models import CommonAll, CommonLocation

# Create your models here.
class Center(CommonAll, CommonLocation):
    logo = models.ImageField(upload_to="centers/logos/")
    website = models.URLField()

    def __str__(self):
        return self.name

class Branch(CommonAll, CommonLocation):
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name="branches")

    def __str__(self):
        return self.name

class Room(CommonAll):
    ROOM_TYPES = (
        ('classroom', 'Classroom'),
        ('reception', 'Reception'),
        ('waiting_area', 'Waiting Area'),
        ('office', 'Office'),
        ('computer_lab', 'Computer Lab'),
    )
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    room_type = models.CharField(max_length=12,  choices=ROOM_TYPES)
    has_projector = models.BooleanField()
    floor = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="rooms")

    def __str__(self):
        return self.name