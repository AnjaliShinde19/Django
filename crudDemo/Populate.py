import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","crudDemo.settings")

import django
django.setup()

from crudApp.models import *
from  faker import Faker
from random import *

faker = Faker()
def Populate(n):
    for i in range(n):
        fsno = randint(1,100)
        fsname = faker.name()
        fsclass = randint(1,10)
        fsaddress = faker.city()

        stud_record = Student.objects.get_or_create(SNo=fsno,SName=fsname,SClass=fsclass,SAddress = fsaddress)

Populate(10)

