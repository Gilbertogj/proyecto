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

## Obras Serializer

class ObrasListSerializer(serializers.ModelSerializer):
  class Meta:
      model = Obra 
      fields = ["id","nombre", "residente"]

class ObrasSerializer(serializers.ModelSerializer):
  class Meta:
      model = Obra 
      fields = "__all__"
  

# Clientes Obras

class ClienteObrasSerializer(serializers.ModelSerializer):
  obras= ObrasListSerializer(many=True)
  class Meta:
      model = Cliente
      fields = [
        "id", 
        "nombre", 
        "alias",
        "direccion", 
        "telefono",
        "created_at",
        "obras",
        ]


# Pedidos

class PedidosListSerializer(serializers.ModelSerializer):
  pedidos_cliente= ClientesListSerializer(many=True)
  class Meta:
      model = Pedido
      fields=["id",
        "pedidos_cliente",

        ] 

class PedidosSerializer(serializers.ModelSerializer):
  class Meta:
      model = Pedido
      fields="__all__"


#Plantas

class PlantasListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Planta
    fields = [
      "id",
      "nombre",

      ]

class PlantasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Planta
    fields = "__all__"














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

