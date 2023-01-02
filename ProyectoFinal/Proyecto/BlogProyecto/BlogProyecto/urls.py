"""BlogProyecto URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from AppBlog.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('AppBlog/about' name='about'),
    path('AppBlog/titulos/', name='titulos'),
    path('AppBlog/titulos/crear', name='crearTitulo'),
    path('AppBlog/titulos/<id>', name='detalleTitulo'),
    path('AppBlog/ titulos/editar/<id>', name='editarTitulo'),
    path('AppBlog/titulos/eliminar/<id>', name='eliminarTitulo'),
    path('AppBlog/ckeditor',),
    path('AppBlog/login/', name='login'),
    path('AppBlog/logout/', name='logout'),
    path('AppBlog/registro/', name='registro'),
    path('AppBlog/perfil/', name='perfil'),
    path('AppBlog/perfil/editar', name='editarPerfil'),
    path('AppBlog/mensajes/',),
    path('AppChat/', name='inicio'),
    path('about/', name='about'),
    path('titulos/' , name='titulos'),
    path('titulos/crear', name='crearTitulo'),
    path('titulos/<id>', name='detalleTitulo'),
    path('titulos/editar/<id>', name='editarTitulo'),
    path('titulos/eliminar/<id>', name='eliminarTitulo'),
    path('ckeditor9',),
    path('login/', name='login'),
    path('logout/', name='logout'),
    path('registro/', name='registro'),
    path('perfil/', name='perfil'),
    path('perfil/editar', name='editarPerfil'),
    path('mensajes/',),
    path('', include('AppBlog.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

