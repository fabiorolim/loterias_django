from django.db import models


# Create your models here.
class MegaSena(models.Model):
    data = models.DateField(auto_now_add=True)
    numeros = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.data} - {str(self.numeros)}'


class Quina(models.Model):
    data = models.DateField(auto_now_add=True)
    numeros = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.data} - {str(self.numeros)}'
