from django.urls import path, include
from AppChat.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path("mensajes/", inicioMensajes, name='mensajes'),
    path("mensajes/<id>", inicioMensajes, name='mensajes'),
    path("leido/<id>", mensajeLeido, name='mensajeLeido'),
       
    
]