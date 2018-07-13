from django.conf.urls import url, include
from . import views
from django.http import HttpResponse
from .models import *
from django.core import serializers
import json

urlpatterns = [
    url(r'^into/', views.test)
]