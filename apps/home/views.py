# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Docentes
from .forms import DocentesForm
from apps.authentication.forms import SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def listardocente(request):
    queryset=request.GET.get("buscar")
    docente = Docentes.objects.all()
    if queryset:
        docente=Docentes.objects.filter(Q(docente__icontains=queryset)).distinct() 
    context={'docente':docente}
    return render(request,"home/docentes/listardocente.html",context)

def agregardocente(request):
    form = DocentesForm()
    if request.method=="POST":
        form= DocentesForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("docentes")
        else:
            form=DocentesForm()
    context={'form':form} 
    return render(request,"home/docentes/agregardocente.html",context) 

def editardocente(request,id):
    if request.method == "POST":
        if id==None:
            form =DocentesForm(request.POST)
        else:
            docente = Docentes.objects.get(pk=id)
            form = DocentesForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
        return redirect("docentes")
    else:
        if id==None:
            form=DocentesForm()
        else:
            docente = Docentes.objects.get(pk = id)
            form = DocentesForm(instance=docente)
        return render(request,"home/docentes/editardocente.html",{'form':form})

def editarperfil(request,id):
    if request.method == "POST":
        if id==None:
            form =SignUpForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        if id==None:
            form=SignUpForm()
        else:
            user = User.objects.get(pk = id)
            form = SignUpForm(instance=user)
        return render(request,"home/editarperfil.html",{'form':form})