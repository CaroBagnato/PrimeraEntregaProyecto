from django import forms

class PostFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    autor=forms.CharField(max_length=40)
    categoria=forms.CharField(max_length=40)

class CategoriasFormulario(forms.Form):
    categoria=forms.CharField(max_length=40)
    subcategoria=forms.CharField(max_length=40)

class AutoresFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    cantidadPosts=forms.IntegerField()
    fecha_ingreso=forms.DateField()
    mail = forms.EmailField(max_length=200)