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
    #Cliente Obras
    RetrieveClienteObrasAPIView
)

urlpatterns = [
    #Clientes
    path("clientes/", ListClientesAPIView.as_view(), name = "list-clientes"),
    path("clientes/<int:pk>/", RetrieveClientesAPIView.as_view(), name = "retrieve-clientes"),
    path("clientes/create/", CreateClientesAPIView.as_view(), name = "create-clientes"),
    path("clientes/<int:pk>/update/", UpdateClientesAPIView.as_view(), name = "update-clientes"),
    path("clientes/<int:pk>/destroy/", DestroyClientesAPIView.as_view(), name = "destroy-clientes"),
    
    #Obras
    path("obras/", ListObrasAPIView.as_view(), name = "list-obras"),
    path("obras/<int:pk>/", RetrieveObrasAPIView.as_view(), name = "retrieve-obras"),

    #Cliente Obras
    path("clientes/<int:pk>/obras/", RetrieveClienteObrasAPIView.as_view(), name = "clientes-Obras"),







]








# router = routers.DefaultRouter()
# router.register(r"clientes", ClientesViewSet)
# router.register(r"obras", ObrasViewSet)
# router.register(r"plantas", PlantasViewSet)
# router.register(r"pedidos", PedidosViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]