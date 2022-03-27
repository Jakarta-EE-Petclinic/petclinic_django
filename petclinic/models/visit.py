from django.db import models

from django.utils import timezone
from django.contrib import admin

from petclinic.models.vet import Vet


class Visit(models.Model):
    datum = models.DateTimeField('date of visit')
    information = models.CharField(max_length=1024)
    vet = models.ForeignKey(
        Vet, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.datum) + " " + self.information
