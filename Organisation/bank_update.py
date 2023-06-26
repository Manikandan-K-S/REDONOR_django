import csv
from Organisation.models import Blood_Banks


def import_data_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row['District']
            name = row['Name']
            contact = row['Contact']
            Blood_Banks.objects.create(city=city, name=name, contact=contact)


import_data_from_csv('blood_banks.csv')
