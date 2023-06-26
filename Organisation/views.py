from django.shortcuts import render
from .models import Blood_Banks
import csv

# Create your views here.


def banks(request):

    blood_banks = Blood_Banks.objects.all()
    return render(request, 'organisation/blood_banks.html', {'blood_banks': blood_banks})
