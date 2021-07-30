from django.urls import path, include
from rest_framework import routers
from .views import (
    #Clientes
    ListClientesAPIView, RetrieveClientesAPIView, 
    CreateClientesAPIView, 
    UpdateClientesAPIView,
    DestroyClientesAPIView,
    #Obras
    ListObrasAPIView, RetrieveObrasAPIView,
    CreateObrasAPIView,
    UpdateObrasAPIView,
    DestroyObrasAPIView,
    #Cliente Obras
    RetrieveClienteObrasAPIView,
    #Plantas
    ListPlantasAPIView,
    RetrievePlantasAPIView,
    CreatePlantasAPIView,
    UpdatePlantasAPIView,
    DestroyPlantasAPIView,
    UpdatePedidosAPIView,
    #Pedidos
    ListPedidosAPIView,
    CreatePedidosAPIView,
    RetrievePedidosAPIView,
    UpdatePedidosAPIView,
    DestroyPedidosAPIView,

    #Users
    CreateUsersAPIView,


)
#comentario 
urlpatterns = [
    #Users
    path("users/create/", CreateUsersAPIView.as_view(), name="create-users"),

    #Clientes
    path("clientes/", ListClientesAPIView.as_view(), name = "list-clientes"),
    path("clientes/<int:pk>/", RetrieveClientesAPIView.as_view(), name = "retrieve-clientes"),
    path("clientes/create/", CreateClientesAPIView.as_view(), name = "create-clientes"),
    path("clientes/<int:pk>/update/", UpdateClientesAPIView.as_view(), name = "update-clientes"),
    path("clientes/<int:pk>/destroy/", DestroyClientesAPIView.as_view(), name = "destroy-clientes"),
    
    #Obras
    path("obras/", ListObrasAPIView.as_view(), name = "list-obras"),
    path("obras/<int:pk>/", RetrieveObrasAPIView.as_view(), name = "retrieve-obras"),
    path("obras/create/", CreateObrasAPIView.as_view(), name = "create-obras"),
    path("obras/<int:pk>/update/", UpdateObrasAPIView.as_view(), name = "update-obras"),
    path("obras/<int:pk>/destroy/", DestroyObrasAPIView.as_view(), name = "destroy-obras"),

    #Cliente Obras
    path("clientes/<int:pk>/obras/", RetrieveClienteObrasAPIView.as_view(), name = "clientes-Obras"),

    #Plantas
    path("plantas/", ListPlantasAPIView.as_view(), name = "list-plantas"),
    path("plantas/<int:pk>/", RetrievePlantasAPIView.as_view(), name = "retrieve-plantas"),
    path("plantas/create/", CreatePlantasAPIView.as_view(), name = "create-plantas"),
    path("plantas/<int:pk>/", UpdatePlantasAPIView.as_view(), name = "update-plantas"),
    path("plantas/<int:pk>/", DestroyPlantasAPIView.as_view(), name = "destroy-plantas"),

    #Pedidos
    path("pedidos/", ListPedidosAPIView.as_view(), name = "list-pedidos"),
    path("pedidos/<int:pk>/", RetrievePedidosAPIView.as_view(), name = "retrieve-pedidos"),
    path("pedidos/create/", CreatePedidosAPIView.as_view(), name = "create-pedidos"),
    path("pedidos/<int:pk>/update/", UpdatePedidosAPIView.as_view(), name = "update-pedidos"),
    path("pedidos/<int:pk>/destroy/", DestroyPedidosAPIView.as_view(), name = "destroy-pedidos"),







]








# router = routers.DefaultRouter()
# router.register(r"clientes", ClientesViewSet)
# router.register(r"obras", ObrasViewSet)
# router.register(r"plantas", PlantasViewSet)
# router.register(r"pedidos", PedidosViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]