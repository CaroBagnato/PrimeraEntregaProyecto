from django.urls import path
from AppDesafio import views

urlpatterns = [
    path("inicio", views.inicio,name='Inicio'),
    path("posts/", views.posts,name='Posts'),
    path("categorias/", views.categorias,name='Categorias'),
    path("autores/", views.autores,name='Autores'),
    path("busqueda/", views.busqueda, name='posts'),
]
