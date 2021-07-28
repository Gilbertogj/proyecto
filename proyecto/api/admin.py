from django.contrib import admin

from .models import Cliente, Obra, Planta, Pedido
# Register your models here.


admin.site.register(Cliente)
admin.site.register(Obra)
admin.site.register(Planta)
admin.site.register(Pedido)
