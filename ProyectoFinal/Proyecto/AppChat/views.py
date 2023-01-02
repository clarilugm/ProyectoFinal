from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from AppBlog.views import obtenerAvatar
from .models import *
from .forms import *
import datetime


@login_required
def inicioMensajes(request, id=None):
    if request.method == 'GET':
        emisor = request.user 
        if id != None: 
            receptor = User.objects.get(id=id) 
            formMensaje = mensajeForm() 
            usuarios = User.objects.all() 
            chat = obtenerChat(request, emisor, receptor)
            return render(request, 'AppChat/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje, 'receptor': receptor, 'chat':chat})
        else:
            formMensaje = mensajeForm()
            usuarios = User.objects.all()
            
    elif request.method == 'POST':
        formMensaje = mensajeForm(request.POST)
        
        if formMensaje.is_valid() and id != None:
            contenido = formMensaje.cleaned_data['contenido']
            emisor = request.user
            receptor = request.POST.get('receptor')
            mensaje = mensajes()
            mensaje.usuarioEmisor = emisor
            mensaje.usuarioReceptor = User.objects.get(id=receptor)
            mensaje.mensaje = contenido
            mensaje.fecha = datetime.datetime.now()

            mensaje.save()
            formMensaje = mensajeForm()
            usuarios = User.objects.all()
            return render(request, 'AppChat/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje, 'mensaje':'Mensaje enviado correctamente!'})
        else:
            formMensaje = mensajeForm()
            usuarios = User.objects.all()
            return render(request, 'AppChat/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje, 'mensaje':'Error al enviar el mensaje, su formulario no es valido'})
    return render(request, 'AppChat/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje})

def obtenerChat(request, emisor, receptor):
    chat= mensajes.objects.filter(usuarioEmisor=emisor, usuarioReceptor=receptor) , mensajes.objects.filter(usuarioEmisor=receptor, usuarioReceptor=receptor).order_by('fecha')
    return chat

def mensajeLeido(request, id=None):
    if request.method == 'GET':
        if id != None:
            mensaje = mensajes.objects.filter(ide=id)
            mensaje.update(leido=True)           
            
            return redirect('mensajes')
        else:
            return redirect('mensajes')
    else:
        return redirect('mensajes')

def mensajeNuevo(request):
    if request.method == 'GET':
        mensajes = mensajes.objects.filter(usuarioReceptor=request.user, leido=False)
        if mensajes:
            return True
        else:
            return False
    else:
        return False
