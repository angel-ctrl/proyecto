from django.db import models

# Create your models here.
class Escritores(models.Model):

    autor = models.CharField(max_length=50)
    libro = models.CharField(max_length=50)

    class Meta:
        verbose_name='Escritor'
        verbose_name_plural='Escritores'
        db_table='Escritor'
        ordering=['id']