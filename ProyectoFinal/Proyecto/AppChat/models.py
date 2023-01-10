from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Mensajes(models.Model):
    id = models.AutoField(primary_key=True)
    usuarioEmisor = models.ForeignKey(User, related_name='usuarioEmisor', on_delete=models.CASCADE) 
    usuarioReceptor = models.ForeignKey(User, related_name='usuarioReceptor', on_delete=models.CASCADE) 
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    leido = models.BooleanField(default=False)
    def __str__(self):
        return self.mensaje

    def getMensaje(self):
        return self.mensaje

    def getFecha(self):
        return self.fecha.strftime('%b %e %Y')

    def getEmisor(self):
        return self.usuarioEmisor.username

    def getReceptor(self):
        return self.usuarioReceptor.username

    def getLeido(self):
        return self.leido