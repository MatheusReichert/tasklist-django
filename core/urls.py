
from django.contrib import admin
from django.urls import path, include 
from .views import home, save, update, deletar
urlpatterns = [
    path('', home),
    path('salvar/', save, name="salvar"),
    path('update/<int:_id>', update, name="update"),
    path('deletar/<int:_id>', deletar, name="deletar"),
]
