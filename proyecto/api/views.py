from rest_framework import viewsets, generics

from .models import Cliente, Obra, Planta, Pedido
from .serializers import ClientesListSerializer, ClientesSerializer 

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#Clinte Views
class ListClientesAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all().order_by("created_at")
    serializer_class = ClientesListSerializer

class CreateClientesAPIView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class RetrieveClientesAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

#Obras Views
class ListClientesAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all().order_by("created_at")
    serializer_class = ClientesListSerializer











# def test (request):
#     """Esta vista prueba"""
#     return HttpResponse("<h1>Test Vistas y urls</h1>")


# ## Cliente Views

# class ClientesViewSet(viewsets.ModelViewSet):
#     """
#     Viewset del modelo Cliente

#     """
#     queryset=Cliente.objects.all()
#     serializer_class= ClientesSerializer

# class ObrasViewSet(viewsets.ModelViewSet):
#     """
#     Viewset del modelo Obra

#     """
#     queryset=Obra.objects.all()
#     serializer_class= ObrasSerializer


# class PlantasViewSet(viewsets.ModelViewSet):
#     """
#     Viewset del modelo Planta

#     """
#     queryset=Planta.objects.all()
#     serializer_class= PlantasSerializer


# class PedidosViewSet(viewsets.ModelViewSet):
#     """
#     Viewset del modelo Pedido

#     """
#     queryset=Pedido.objects.all()
#     serializer_class= PedidosSerializer

