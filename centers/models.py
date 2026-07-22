from django.db import models

# Create your models here.
class CommonAll(models.Model):
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CommonLocation(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Centers(CommonAll, CommonLocation):
    logo = models.ImageField(upload_to="centers/logos/")
    website = models.URLField()

    def __str__(self):
        return self.name

class Branch(CommonAll, CommonLocation):
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    center = models.ForeignKey(Centers, on_delete=models.CASCADE, related_name="branch")

    def __str__(self):
        return self.name