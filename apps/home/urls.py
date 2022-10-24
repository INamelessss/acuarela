# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import imp
from django.urls import path, re_path
from apps.authentication.views import agregarusuario, editarusuario, listarusuario
from apps.home import views
from .views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path('usuarios/',listarusuario ,name="usuarios"),
    path('usuarios/agregar',agregarusuario ,name="adduser"),
    path('usuarios/editar/<int:id>/',editarusuario ,name="edituser"),
    path('docentes/',listardocente,name="docentes"),
    path('docentes/agregar',agregardocente,name="adddocente"),
    path('docentes/editar/<int:id>/',editardocente,name="editdocente"),
    path('perfil/<int:id>/',editarperfil,name="perfil"),
]
