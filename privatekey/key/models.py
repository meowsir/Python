from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=20);
    account = models.CharField(max_length=30);
    password = models.CharField(max_length=30);