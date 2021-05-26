from django.urls import path, include
from rest_framework import routers
from .views import ListClientesAPIView, RetrieveClientesAPIView, CreateClientesAPIView

urlpatterns = [
    #List and Retrieve Clientes
    path("clientes/", ListClientesAPIView.as_view(), name = "list-clientes"),
    path("clientes/<int:pk>/", RetrieveClientesAPIView.as_view(), name = "retrieve-clientes"),
    #Create Clientes
    path("clientes/create/", CreateClientesAPIView.as_view(), name = "create-clientes"),





]








# router = routers.DefaultRouter()
# router.register(r"clientes", ClientesViewSet)
# router.register(r"obras", ObrasViewSet)
# router.register(r"plantas", PlantasViewSet)
# router.register(r"pedidos", PedidosViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]