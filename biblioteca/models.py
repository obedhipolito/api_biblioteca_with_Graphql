from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es necesario para crear un usuario')
        user = self.model(correo=self.normalize_email(correo), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.TextField(default='', blank=False)
    a_paterno = models.TextField(default='', blank=False)
    a_materno = models.TextField(default='', blank=False)
    tipoDeUsuario = models.TextField(default='', blank=False)
    ciudad = models.TextField(default='', blank=False)
    correo = models.EmailField(default='', unique=True, blank=False)
    password = models.TextField(default='', blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'a_paterno', 'a_materno', 'tipoDeUsuario', 'ciudad']


class Autor(models.Model):
    nombre = models.TextField(default='', blank=False)
    a_paterno = models.TextField(default=0, blank=False)
    a_materno = models.TextField(default=0, blank=False)
    fechaNacimiento = models.DateField(default=0, blank=False)
    nacionalidad = models.TextField(default='', blank=False)
    biografia = models.TextField(default='', blank=False)

class Coleccion(models.Model):
    id_Autor = models.ForeignKey(Autor, null=True, on_delete=models.CASCADE)
    titulo = models.TextField(default='', blank=False)
    isbn = models.IntegerField(default='', blank=False)
    tipoDeColeccion = models.TextField(default='', blank=False)
    descripcion = models.TextField(default='', blank=False)
    fechaPublicacion = models.DateField(default='', blank=False)
    categoria = models.TextField(default='', blank=False)
    estado = models.TextField(default='', blank=False)
    ubicacioEnBiblioteca = models.TextField(default='', blank=False)
    precio = models.FloatField(default='', blank=False)

class Inventario(models.Model):
    id_Coleccion = models.ForeignKey(Coleccion, null=True, on_delete=models.CASCADE)
    cantidadDisponible = models.IntegerField(default='', blank=False)
    cantidadTotal = models.IntegerField(default='', blank=False)
    fechaDeAdquisicion = models.DateField(default='', blank=False)

class CatalogoEnLinea(models.Model):
    id_coleccion = models.ForeignKey(Coleccion, null=True, on_delete=models.CASCADE)
    id_inventario = models.ForeignKey(Inventario, null=True, on_delete=models.CASCADE)
    enlace = models.TextField(default='', blank=False)

class Prestamo(models.Model):
    id_usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    id_coleccion = models.ForeignKey(Coleccion, null=True, on_delete=models.CASCADE)
    fechaInicio = models.DateField(default='', blank=False)
    fechaVencimiento = models.DateField(default='', blank=False)
    fechaDevolucion = models.DateField(default='', blank=False)
    estadoPrestamo = models.TextField(default='', blank=False)

class Reserva(models.Model):
    id_usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    id_coleccion = models.ForeignKey(Coleccion, null=True, on_delete=models.CASCADE)
    fechaReserva = models.DateField(default='', blank=False)
    estadoReserva = models.TextField(default='', blank=False)

class misCosas(models.Model):
    id_usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    id_coleccion = models.ForeignKey(Coleccion, null=True, on_delete=models.CASCADE)
    fechaAdquisicion = models.DateField(default='', blank=False)
    