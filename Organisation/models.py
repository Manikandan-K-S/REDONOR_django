from django.db import models

# Create your models here.


class Blood_Banks(models.Model):
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, default=None)
