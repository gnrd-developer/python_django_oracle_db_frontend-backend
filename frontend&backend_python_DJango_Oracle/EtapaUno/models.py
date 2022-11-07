from django.db import models

# Create your models here.
class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name='Id de comuna')
    nombreComuna = models.CharField(max_length=50, verbose_name='Nombre de la Comuna')

    def __str__(self):
        return self.nombreComuna

class Publicacion(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='Id')
    lapublicacion = models.TextField(max_length=1000, verbose_name='lapublicacion')
    fecha = models.DateField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.id





