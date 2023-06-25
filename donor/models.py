from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Donor_detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    bloodgroup = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    city = models.CharField(max_length=25)
