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

    class Meta:
        abstract = True

class CommonIndividuals(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=53)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()

    class Meta:
        abstract = True