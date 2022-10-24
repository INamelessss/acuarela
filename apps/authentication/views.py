# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.template import loader
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def listarusuario(request):
    queryset=request.GET.get("buscar")
    user = User.objects.all()
    if queryset:
        user=User.objects.filter(Q(user__icontains=queryset)).distinct() 
    context={'user':user}
    return render(request,"home/userlist.html",context)

def agregarusuario(request):
    form = SignUpForm()
    if request.method=="POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("usuarios")
        else:
            form=SignUpForm()
    context={'form':form} 
    return render(request,"home/agregaruser.html",context) 

def editarusuario(request,id):
    if request.method == "POST":
        if id==None:
            form =SignUpForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect("usuarios")
    else:
        if id==None:
            form=SignUpForm()
        else:
            user = User.objects.get(pk = id)
            form = SignUpForm(instance=user)
        return render(request,"home/editaruser.html",{'form':form})