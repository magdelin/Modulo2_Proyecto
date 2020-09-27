from django.db import models

# Create your models here.

class Pasajero(models.Model):
    Nombre = models.CharField(max_lenght=100, null= False, blank=False,verbose_name='Nombre')
    Apellido = models.CharField(max_lenght=100, null= False, blank=False,verbose_name='Apellido')
    Pasaporte = models.CharField(max_lenght=100, null= False, blank=False, unique = True,verbose_name='Pasaporte')
    Telefono = models.CharField(max_lenght=100, null= True, blank=True, unique = False,verbose_name='Telefono')
    DOB = models.DateField(auto_now_add=False,auto_now= False, verbose_name='DOB')
    genders = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    Sexo = models.CharField(max_length=1, choices=genders,verbose_name='Sexo')
    Email = models.EmailField(max_length=200, verbose_name='Email')
    Nacionalidad = models.CharField(max_lenght=100, null= False, blank=False,verbose_name='Nacionalidad')  
