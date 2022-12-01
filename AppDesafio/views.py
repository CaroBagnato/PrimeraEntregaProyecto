from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from AppDesafio.models import Post
from AppDesafio.models import Categorias
from AppDesafio.models import Autores

from AppDesafio.forms import CategoriasFormulario
from AppDesafio.forms import PostFormulario
from AppDesafio.forms import AutoresFormulario

def busqueda(request):
    busqueda = request.GET.get('post')
    print(busqueda)
    posta = Post.objects.filter(nombre = busqueda)
    return render(request,'AppDesafio/resultadoposts.html',{"busqueda": busqueda, "posta": posta})

# Create your views here.
def inicio(request):
    return render(request,'AppDesafio/inicio.html')    

def posts(request):
        if request.method == "POST":
            postForms = PostFormulario(request.POST)
            print(postForms)

            if postForms.is_valid:
                informacion = postForms.cleaned_data
                post = Post(nombre=informacion["nombre"], autor=informacion["autor"], categoria=informacion["categoria"])
                post.save()
                return render(request, "AppDesafio/inicio.html")
        else:
            postForms = PostFormulario()

        return render(request,'AppDesafio/posts.html', {'postForms':postForms})  


def categorias(request):
        if request.method == "POST":
            categoriasForms = CategoriasFormulario(request.POST)
            print(categoriasForms)

            if categoriasForms.is_valid:
                informacion = categoriasForms.cleaned_data
                categoria = Categorias(categoria=informacion["categoria"], subcategoria=informacion["subcategoria"])
                categoria.save()
                return render(request, "AppDesafio/inicio.html")
        else:
            categoriasForms = CategoriasFormulario()

        return render(request,'AppDesafio/categorias.html', {'categoriasForms':categoriasForms}) 
    
def autores(request):  
        if request.method == "POST":
            autoresForms = AutoresFormulario(request.POST)
            print(autoresForms)

            if autoresForms.is_valid:
                informacion = autoresForms.cleaned_data
                autores = Autores(nombre=informacion["nombre"], cantidadPosts=informacion["cantidadPosts"], fecha_ingreso=informacion["fecha_ingreso"], mail=informacion["mail"])
                autores.save()
                return render(request, "AppDesafio/inicio.html")
        else:
            autoresForms = AutoresFormulario()

        return render(request,'AppDesafio/Autores.html', {'autoresForms':autoresForms})