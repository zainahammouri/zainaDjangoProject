import datetime
from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Patients(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    

#All of our Center
class Appointments(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.RESTRICT)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='images/Appointments/'),

    def __str__(self):
        return self.description
    

#patients Orders
class Order(models.Model):
    appointmint=models.ForeignKey(Appointments, on_delete=models.RESTRICT)
    patients=models.ForeignKey(Patients, on_delete=models.RESTRICT)
    date=models.DateTimeField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.appointmint
