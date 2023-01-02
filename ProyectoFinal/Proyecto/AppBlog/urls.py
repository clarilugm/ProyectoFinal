from django.urls import path, include
from AppBlog.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name='inicio'),
    path("about/", about, name="about"),
    path("titulos/", titulos, name="titulos"),
    path("titulos/crear",crearTitulo, name="crearTitulo"),
    path("titulos/<id>", detallesTitulo, name="detalleTitulo"),
    path("titulos/editar/<id>", editarTitulo, name="editarTitulo"),
    path("titulos/eliminar/<id>", eliminarTitulo, name="eliminarTitulo"),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path("login/", login_request, name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("registro/", registroUsuario, name='registro'),
    path("perfil/", perfilUsuario, name='perfil'),
    path("perfil/editar", editarPerfil, name='editarPerfil'),
    path("mensajes/", include('AppChat.urls'), name='mensajes'),
    
]

