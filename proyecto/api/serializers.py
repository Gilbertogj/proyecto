from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Obra, Planta, Pedido

## Cliente Serializers

class ClientesListSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cliente
      fields=["id", "nombre", "alias", "created_at"]


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
  
  class Meta:
      model = Pedido
      fields=["id",
   

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


#Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        print(validate_data)
        user = User.objects.create_user(**validate_data)

        return user












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

