from rest_framework import viewsets

from .models import Cliente, Obra, Planta, Pedido
from .serializers import ClienteSerializer, ObraSerializer, PlantaSerializer, PedidoSerializer

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test (request):
    """Esta vista prueba"""
    return HttpResponse("<h1>Test Vistas y urls</h1>")


## Cliente Views

class ClientesViewSet(viewsets.ModelViewSet):
    """
    Viewset del modelo Cliente

    """
    queryset=Cliente.objects.all()
    serializer_class= ClienteSerializer

class ObrasViewSet(viewsets.ModelViewSet):
    """
    Viewset del modelo Obra

    """
    queryset=Obra.objects.all()
    serializer_class= ObraSerializer


class PlantasViewSet(viewsets.ModelViewSet):
    """
    Viewset del modelo Planta

    """
    queryset=Planta.objects.all()
    serializer_class= PlantaSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    """
    Viewset del modelo Pedido

    """
    queryset=Pedido.objects.all()
    serializer_class= PedidoSerializer

