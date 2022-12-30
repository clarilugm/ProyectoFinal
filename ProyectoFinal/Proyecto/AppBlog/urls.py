from django.urls import path, include
from AppBlog.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name='inicio'),
    path("about/", about, name="about"),
    path("titulos/add",crearTitulo, name="crearTitulo"),
    path("titulos/", titulos, name="titulos"),
    path("titulos/<ide>", detallesTitulo, name="detalleTitulo"),
    path("titulos/editar/<ide>", editarTitulo, name="editarTitulo"),
    path("titulos/eliminar/<ide>", eliminarTitulo, name="eliminarTitulo"),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path("login/", login_request, name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("registro/", registroUsuario, name='registro'),
    path("perfil/", perfilUsuario, name='perfil'),
    path("perfil/editar", editarPerfil, name='editarPerfil'),
    path("mensajes/", include('AppMensajeria.urls'), name='mensajes'),
    
]

