"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppBlog.urls import *
from AppChat.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBlog/', include('AppBlog.urls')),
    path('AppChat/', include('AppChat.urls')),
    path('', inicio, name= 'Inicio'),
    path('AppBlog/login/', login_request, name= 'Login'),
    path('AppBlog/registro/', registroUsuario, name = 'Registro'),
    path('AppBlog/logout/', LogoutView.as_view, name ='Logout' ),
    path('perfil/', perfilUsuario, name= 'perfil'),
    path('about/', about, name = 'about'),
    path('crearTitulo/', crearTitulo, name='nuevo titulo'), 
    path('detalles/<ide>/', detallesTitulo, name = 'detalles titulo'), 
    path('editar/<pk>', editarTitulo, name= 'editar titulo'),
    path('borrar/<pk>', eliminarTitulo, name = 'eliminar titulo'),
    path('inicioMensaje/' , inicioMensajes, name = 'mensajes'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)