# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Docentes(models.Model):
    id=models.AutoField(primary_key=True)
    ap_paterno=models.CharField(max_length=30)
    ap_materno=models.CharField(max_length=30)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=9)
    activo=models.BooleanField(default=True)
