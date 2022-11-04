from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' ' + self.carmodel


class Customer:
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.Customer


class Employee:
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=3)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name + ' ' + self.Employee


