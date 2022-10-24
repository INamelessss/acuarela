# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import imp
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
import re
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.db import models
from core.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth import get_user_model
