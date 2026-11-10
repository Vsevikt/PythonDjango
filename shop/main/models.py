from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField()

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    refresh_token = models.CharField(max_length=200, null=True, blank=True)
