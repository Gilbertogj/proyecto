from rest_framework import serializers

from .models import Cliente, Obra, Planta, Pedido

## Cliente Serializers

class ClientesListSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cliente
      fields=["id", "nombre", "alias"]


class ClientesSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cliente
      fields="__all__"











# class ClientesSerializer(serializers.ModelSerializer) :
#   class Meta:
#     model = Cliente
#     fields = '__all__'

# class ObrasSerializer(serializers.ModelSerializer) :
#   class Meta:
#     model = Obra
#     fields = '__all__'
    
# class PlantasSerializer(serializers.ModelSerializer) :
#   class Meta:
#     model = Planta
#     fields = '__all__'

# class PedidosSerializer(serializers.ModelSerializer) :
#   class Meta:
#     model = Pedido
#     fields = '__all__'

