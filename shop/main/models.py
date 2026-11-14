from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cards/')
    created_at = models.DateTimeField()

class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    refresh_token = models.CharField(max_length=200, null=True, blank=True)
