from django.urls import path, include
from rest_framework import routers
from .views import ClientesViewSet, ObrasViewSet, PlantasViewSet, PedidosViewSet

router = routers.DefaultRouter()
router.register(r"clientes", ClientesViewSet)
router.register(r"obras", ObrasViewSet)
router.register(r"plantas", PlantasViewSet)
router.register(r"pedidos", PedidosViewSet)

urlpatterns = [
    path("", include(router.urls)),
]