from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test (request):
    """Esta vista prueba"""
    return HttpResponse("<h1>Test Vistas y urls</h1>")


