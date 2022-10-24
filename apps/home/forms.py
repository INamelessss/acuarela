from dataclasses import field
import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Docentes

class DocentesForm(forms.ModelForm):
    class Meta:
        model= Docentes
        fields = ['ap_paterno','ap_materno','nombre','telefono']
