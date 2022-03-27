from django.db import models


from petclinic.models.pettype import PetType
from petclinic.models.visit import Visit


class Pet(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth')
    pet_type = models.ForeignKey(
        PetType, on_delete=models.CASCADE
    )
    visits = models.ManyToManyField(Visit)

    def __str__(self):
        return self.name + " " + str(self.date_of_birth)


