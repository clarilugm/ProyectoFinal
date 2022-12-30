from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField


class BlogForm(forms.Form):

    titulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Su título aquí: "}), 
            help_text=("Máximo de caracteres por título 60"), 
            max_length=100, required=True)

    subtitulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Subtitulo: "}), 
              help_text=("Máximo de caracteres por subtitulo 60"),
              max_length=100, required=True)

    fecha = forms.DateTimeField(widget=forms.TextInput(attrs={"class":"form-control", "type":"date"}) , required=True)

    contenido = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Blog
        fields = ('titulo', 'fecha', 'contenido', 'imagen', 'subtitulo', 'usuarioFK')
        widgets = {
            'contenido': CKEditorWidget(),
        }
    
    imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={"class":"form-control"}), required=True)

class registroUsuarioForm(UserCreationForm):
    username = forms.CharField(label="Usuario: ", 
    widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Nombre de usuario:", "required":True, "autofocus":True, "class":"form-control"}),
    help_text=("Escoja un usuario con mas de 4 caracteres.")
                                )
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese su email: ","class":"form-control"}),
            help_text=(".........")) #ver bien
    password1= forms.CharField(label="Ingrese una contraseña: ",
               widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":" Ingrese su contraseña", "class":"form-control"}),
               help_text=("Contraseña con al menos 8 caracteres, con números."))

    password2= forms.CharField(label="Confirme su contraseña: ", 
               widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":" Confirme su contraseña: ", "class":"form-control"}),
               help_text=("Verifique que las contraseñas coincidan."))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AuthUsuario(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True , "class":"form-control", "placeholder":" Ingrese su nombre de usario: "}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"form-control", "placeholder":" Ingrese su contraseña: "})
    )

class EditartPerfilForm(forms.Form):
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Nombre:"}), required=True, max_length=20)
    apellido = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"  Apellido: "}), required=True, max_length=20)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Email: ","class":"form-control"}),
             help_text=("example@example.com"))
    class Meta:
        model = User
        fields = ["firstName", "lastName", "username","email", ]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={"class":"form-control"}), required=True)