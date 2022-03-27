from django.db import models

from .pet import Pet


class Owner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.city
