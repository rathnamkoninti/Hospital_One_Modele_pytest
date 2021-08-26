import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Hospital.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fename = fake.name()
        fphonenumber=phonenumbergen()
        hospital_record=Hospital.objects.get_or_create(name=fename,mobile=fphonenumber)

populate(25)
