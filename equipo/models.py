from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    youtube = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    email = models.EmailField(  blank=True)
    logo = models.ImageField(verbose_name="logo", upload_to="images/empresa", blank=True)

class Asesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=20)
    apeido = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    foto = models.ImageField(verbose_name="perfil", upload_to="images/user", blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        user = self.nombre + " " + self.apeido
        return user


class Citas(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    whattsapp = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.nombre_completo