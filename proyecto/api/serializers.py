from rest_framework import serializers

from .models import Cliente, Obra, Planta, Pedido

## Cliente Serializers

class ClienteSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Cliente
    fields = '__all__'

class ObraSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Obra
    fields = '__all__'
    
class PlantaSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Planta
    fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Pedido
    fields = '__all__'

