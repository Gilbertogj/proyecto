from rest_framework import viewsets, generics

from .models import Cliente, Obra, Planta, Pedido
from .serializers import (
    ClientesListSerializer, 
    ClientesSerializer, 
    ObrasListSerializer, 
    ObrasSerializer,
    ClienteObrasSerializer, 
    PedidosListSerializer,
    PedidosSerializer,
    PlantasListSerializer,
    PlantasSerializer,
) 

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

class UpdateClientesAPIView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class DestroyClientesAPIView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

#Obras Views
class ListObrasAPIView(generics.ListAPIView):
    queryset = Obra.objects.all().order_by("created_at")
    serializer_class = ObrasListSerializer

class RetrieveObrasAPIView(generics.RetrieveAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObrasSerializer

class CreateObrasAPIView(generics.CreateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObrasSerializer

class UpdateObrasAPIView(generics.UpdateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObrasSerializer

class DestroyObrasAPIView(generics.DestroyAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObrasSerializer



#Obras de Cliente

class RetrieveClienteObrasAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteObrasSerializer

#Planta

class ListPlantasAPIView(generics.ListAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantasListSerializer

class RetrievePlantasAPIView(generics.RetrieveAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantasSerializer

class CreatePlantasAPIView(generics.CreateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantasSerializer

class UpdatePlantasAPIView(generics.UpdateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantasSerializer

class DestroyPlantasAPIView(generics.DestroyAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantasSerializer



#Pedidos

class ListPedidosAPIView(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidosListSerializer

class CreatePedidosAPIView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidosSerializer











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

