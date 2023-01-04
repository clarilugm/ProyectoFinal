from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 


def inicio(request):
      titulos = Blog.objects.all().order_by('-fecha')
      return render(request, 'AppBlog/inicio.html', {'titulos':titulos, 'avatar':obtenerAvatar(request)})
    
def about(request):
    return render(request, 'AppBlog/about.html', {'avatar':obtenerAvatar(request)})

login_required #!
def crearTitulo(request):
    
    if request.method == 'POST' and request.FILES['imagen']:

        form = BlogForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            ObjectBlog = Blog()
            ObjectBlog.titulo = form.cleaned_data['titulo']
            ObjectBlog.subtitulo = form.cleaned_data['subtitulo']
            ObjectBlog.fecha = form.cleaned_data['fecha']
            ObjectBlog.contenido = form.cleaned_data['contenido']
            ObjectBlog.imagen = form.cleaned_data['imagen']
            ObjectBlog.usuarioFK = request.user
            ObjectBlog.save()
            return render(request, 'AppBlog/crearTitulo.html', { 'form':form, 'mensaje':'Su nuevo título se cargó correctamente! :)', 'avatar':obtenerAvatar(request)})
        else:
            form = BlogForm(initial={})
            return render(request, 'AppBlog/crearTitulo.html', { 'form':form, 'mensaje':'Hubo un error al cargar su título. :(', 'avatar':obtenerAvatar(request)})

    else:
        form = BlogForm(initial={})
        
    return render(request, 'AppBlog/crearTitulo.html', {'form':form, 'avatar': obtenerAvatar(request)} )


def titulos(request):
    titulos = Blog.objects.all().order_by('-fecha')
    return render(request, 'AppBlog/titulos.html', {'titulos':titulos, 'avatar':obtenerAvatar(request)})

@login_required
def editarTitulo(request, ide):
    if request.method == 'POST':
        titulos = Blog.objects.get(ide=ide)
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            titulos.titulo = form.cleaned_data['titulo']
            titulos.subtitulo = form.cleaned_data['subtitulo']
            titulos.fecha = form.cleaned_data['fecha']
            titulos.contenido = form.cleaned_data['contenido']
            titulos.imagen = form.cleaned_data['imagen']
            titulos.save()
            return render(request, 'AppBlog/editarTitulo.html', {'form':form, 'mensaje':'Editó su título.', 'titulo':titulo, 'avatar':obtenerAvatar(request)})
        else:
            return render(request, 'AppBlog/editarTitulo.html', {'form':form, 'mensaje':'No se pudo editar el título.', 'titulo':titulo, 'avatar':obtenerAvatar(request)})
    else:
        titulo = Blog.objects.get(ide=ide)
        form = BlogForm(initial={'titulo':titulo.titulo, 'subtitulo': titulo.subtitulo, 'fecha':titulo.fecha, 'contenido':titulo.contenido, 'imagen':titulo.imagen})
        return render(request, 'AppBlog/editarTitulo.html', {'form':form, 'mensaje':'Titulo editado correctamente', 'titulo':titulo, 'avatar':obtenerAvatar(request)})


def detallesTitulo(request, ide):
    if request.method == 'GET':
        blog = Blog.objects.filter(ide=ide)
        if blog:
            titulo = Blog.objects.get(ide=ide)
            fecha = titulo.fecha.strftime("%d %B, %Y")
            user = titulo.usuarioFK
            autor = User.objects.get(username=user)
            return render(request, 'AppBlog/detallesTitulo.html', {'titulo':titulo ,'fecha_format':fecha, 'autor':autor, 'avatar':obtenerAvatar(request) } )
        else:
            return render(request, 'AppBlog/detallesTitulo.html', {'mensaje':'No hay más títulos disponibles.', 'avatar':obtenerAvatar(request)} )

    return render(request, 'AppBlog/detallesTitulo.html', {'mensaje':'No hay más títulos.', 'avatar':obtenerAvatar(request)})

@login_required
def eliminarTitulo(request, ide):
    if request.method == 'GET':
        titulos = Blog.objects.get(ide=ide)
        titulos.delete()
        return render(request, 'AppBlog/titulos.html', {'mensaje':'Título eliminado correctamente', 'avatar':obtenerAvatar(request)})
    else:
        return render(request, 'AppBlog/titulos.html', {'mensaje':'Error al eliminar este título.', 'avatar':obtenerAvatar(request)})

def login_request(request):
    if request.method == 'POST':
        form = AuthUsuario(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil') 
            else:
                return render(request, 'AppBlog/login.html', {'form':form, 'mensaje':'Su usuario y contraseña no coinciden'})
        else:
                return render(request, 'AppBlog/login.html', {'form':form, 'mensaje':'Su usuario y contraseña no coinciden'})
    else:
        form = AuthUsuario()
    return render(request, 'AppBlog/login.html', {'form':form} )

@login_required 
def perfilUsuario(request):
    if request.method == 'POST':
        avatarForm = AvatarForm(request.POST, request.FILES)
        if avatarForm.is_valid():
            avatarViejo = Avatar.objects.filter(usuarioFK=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar = Avatar(usuarioFK=request.user, imagen=avatarForm.cleaned_data['imagen'] )
            avatar.save()
            avatarForm = AvatarForm()
            mensajeNuevo = mensajeNuevo(request)
            return render(request, 'AppBlog/perfil.html' , {'user':request.user , 'avatar':obtenerAvatar(request), 'avatarForm':avatarForm, 'mensaje':'Te damos la bienvenida a tu perfil!', 'mensaje_avatar_form':'Su foto de perfil fue actualizada exitosamente', 'mensajeNuevo':nuevoMensaje})
        else:
            avatarForm = AvatarForm()
            nuevoMensaje = mensajeNuevo(request)
            return render(request, 'AppBlog/perfil.html' , {'user':request.user,  'avatar':obtenerAvatar(request), 'avatarForm':avatarForm, 'mensaje':'Te damos la bienvenida a tu perfil', 'mensaje_avatar_form':'Error al actualizar la imagen de perfil', 'mensajeNuevo':nuevoMensaje})

    else:
        avatarForm = AvatarForm()
        nuevoMensaje = mensajeNuevo(request)
        return render(request, 'AppBlog/perfil.html' , {'user':request.user , 'avatar':obtenerAvatar(request) ,'avatarForm':avatarForm, 'mensaje':'Te damos la bienvenida a tu perfil', 'mensajeNuevo':nuevoMensaje})

def editarPerfil(request):
    if request.method == 'POST':
        form = EditartPerfilForm(request.POST)
        if form.is_valid():
            user = request.user
            user.firstName = form.cleaned_data['nombre']
            user.lastName = form.cleaned_data['apellido']
            user.email = form.cleaned_data['email']
            user.save()
            form = EditartPerfilForm()
            return render(request, 'AppBlog/editarPerfil.html', {'form':form, 'mensaje':'Sus datos fueron actualizados correctamente :)', 'avatar':obtenerAvatar(request)})
        else:
            form = EditartPerfilForm()
            return render(request, 'AppBlog/editarPerfil.html', {'form':form, 'mensaje':'Hubo un error a la hora de actualizar sus datos :(', 'avatar':obtenerAvatar(request)})
    else:
        form = EditartPerfilForm()
    return render(request, 'AppBlog/editarPerfil.html', {'form':form, 'avatar':obtenerAvatar(request)})

def obtenerAvatar(request):
    try: #!!!!
        lista=Avatar.objects.filter(usuarioFK=request.user) 
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen="/media/avatar/avatarpordefecto.png"
        return imagen
    except:
        return "/media/avatar/avatarpordefecto.png"



def registroUsuario(request):
    if request.method == 'POST':
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'AppBlog/registro.html', {'form':form, 'mensaje':'Usuario registrado correctamente.', 'avatar':obtenerAvatar(request)})
        else:
            error = form.errors
            form = registroUsuarioForm()    
            return render(request, 'AppBlog/registro.html', {'form':form, 'mensaje':'Error al registrar su usuario.', 'error':error})
    else:
        form = registroUsuarioForm()
    return render(request, 'AppBlog/registro.html', {'form':form} )

def mensajeNuevo(request):
    if request.method == 'GET':
        mensajes = mensajes.objects.filter(userDestinatario=request.user, leido=False)
        if mensajes:
            return True
        else:
            return False
    else:
        return False