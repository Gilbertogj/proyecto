from django.db import models
from decimal import Decimal

#Relations
# 1 Cliente - N Obra
# 1 Cliente - N Pedido
# 1 Obra - N Pedido
# 1 Planta - N Pedido


# Create your models here.
class Cliente(models.Model):
    """Cliente model."""
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    rfc = models.TextField(max_length=100, unique=True)
    METODO_PAGO = (
        ("F", "F"),
        ("G", "G"),
    )
    PAGO = models.CharField(max_length=5, choices=METODO_PAGO) 
    direccion = models.TextField(max_length=1000)
    telefono = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)  
    sitio_web = models.TextField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.nombre} {self.alias}"


class Obra(models.Model):
    """Obra model."""
    nombre = models.CharField(max_length=255)
    residente = models.CharField(max_length=255)
    direccion = models.TextField(max_length=1000)
    telefono = models.CharField(max_length=25)
    email = models.EmailField(unique=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="obras"
    )

    def __str__(self):
        return f"{self.nombre} {self.residente} cliente:{self.cliente.nombre}"


class Planta(models.Model):
    """Planta model."""
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(max_length=1000)
    telefono = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.direccion}"


class Pedido(models.Model):
    """Cliente model."""

    metros_cubicos = models.DecimalField(max_digits=10, decimal_places= 2)

    TIPO_CONCRETO = (
        ("C", "Convencional"),
        ("R", "Rápido"),
        ("LZ", "Lanzado"),
        ("AR", "Arquitectónico"),
        ("RF", "Relleno Fluido"),
        ("MO", "Mortero"),
        ("ES", "Estructurales"),
        ("AU", "Autocompactables"),
    )
    tipo = models.CharField(max_length=30, choices=TIPO_CONCRETO)

    RESISTENCIA = (
        ("25", "25"),
        ("50", "50"),
        ("75", "75"),
        ("150", "150"),
        ("100", "100"),
        ("200", "200"),
        ("250", "250"),
        ("300", "300"),
        ("350", "350"),
        ("400", "400"),
        ("650", "650"),
    )
    resistencia = models.CharField(max_length=10, choices=RESISTENCIA)

    EDAD = (
        ("R01", "R01"),
        ("R03", "R03"),
        ("R07", "R07"),
        ("R14", "R14"),
        ("N", "N"),
    )
    edad = models.CharField(max_length=10, choices=EDAD)

    TAMAÑO_NOMINAL= (
        ("10", "3/8 10mm"),
        ("20", "3/4 20mm"),
        ("40", "1 1/12 40mm"),
        ("05", "Arena 05mm"),
    )
    tma = models.CharField(max_length=20, choices=TAMAÑO_NOMINAL)

    REVENIMIENTO= (
        ("06", "06 cm"),
        ("08", "08 cm"),
        ("10", "10 cm"),
        ("12", "12 cm"),
        ("14", "14 cm"),
        ("16", "16 cm"),
        ("18", "18 cm"),
        ("20", "20 cm"),
        ("22", "22 cm"),
    )
    revenimiento = models.CharField(max_length=20, choices=REVENIMIENTO)

    FORMA= (
        ("T", "Tirado"),
        ("B", "Bombeado"),
    )
    forma = models.CharField(max_length=10, choices=FORMA)
    
    TIPO_BOMBA= (
        ("Pluma", "Bomba Pluma"),
        ("Estacionaria", "Bomba Estacionaria"),
    )
    tipo_bomba = models.CharField(max_length=20, choices=TIPO_BOMBA)

    NUMERO_BOMBA= (
        ("BC-03 Pluma", "BC-03 Pluma Chica"),
        ("BC-04 Pluma", "BC-04 Pluma"),
        ("BC-05 Pluma", "BC-05 Pluma"),
        ("BC-06 Estacionaria", "BC-06 Estacionaria"),
        
    )
    numero_bomba = models.CharField(max_length=30, choices=NUMERO_BOMBA)
    metros_adicionales = models.CharField(max_length=255)

    ADITIVO= (
        ("Autocompactable", "Autocompactable"),
        ("Autocurable", "Autocurable"),
        ("Fibra de acero", "Fibra de acero"),
        ("Fibra de polipropileno", "Fibra de polipropileno"),
        ("Fluidizante", "Fluidizante"),
        ("Impermeabilizante al 1%", "Impermeabilizante al 1%"),
        ("Impermeabilizante al 2%", "Impermeabilizante al 2%"),
        ("Impermeabilizante al 4%", "Impermeabilizante al 4%"),
        ("Inclusor de aire", "Inclusor de aire"),
        ("Perlita de polipropileno", "Perlita de polipropileno"),
        ("Plastificantes", "Plastificantes"),
        ("Retardante", "Retardante"),
        ("Ninguno", "Ninguno"),
        
    
    )
    aditivo = models.CharField(max_length=30, choices=ADITIVO)

    ELEMENTO_COLAR= (
        ("Arroyo", "Arroyo"),
        ("Ballenas", "Ballenas"),
        ("Cabezales", "Cabezales"),
        ("Castillos", "Castillos"),
        ("Cimentación", "Cimentación"),
        ("Columnas", "Columnas"),
        ("Contra trabes", "Contra trabes"),
        ("Dados", "Dados"),
        ("Diamantes", "Diamantes"),
        ("Encofrado", "Encofrado"),
        ("Escaleras", "Escaleras"),
        ("Firme", "Firme"),
        ("Firme pulido", "Firme pulido"),
        ("Guarnición", "Guarnición"),
        ("Huellas", "Huellas"),
        ("Losa de azotea", "Losa de azotea"),
        ("Losa de entre piso", "Losa de entre piso"),
        ("Losa primer piso", "Losa primer piso"),
        ("Losa segundo piso", "Losa segundo piso"),
        ("Losacero", "Losacero"),
        ("Muro de contención", "Muro de contención"),
        ("Muros de carga", "Muros de carga"),
        ("Nivelación de losa", "Nivelación de losa"),
        ("Piso pulido", "Piso pulido"),
        ("Rampa de acceso", "Rampa de acceso"),
        ("Talud", "Talud"),
        ("Zapata corrida", "Zapata corrida"),
        ("Zapatas", "Zapatas"),
    )
    elemento_colar = models.CharField(max_length=255, choices=ELEMENTO_COLAR)
    observaciones = models.CharField(max_length=255)
    fecha_pedido = models.DateTimeField()

    STATUS_TYPE= (
        ("Activado", "Activado"),
        ("Desactivado", "Desactivado"),
    )
    status= models.CharField(max_length=25, choices=STATUS_TYPE, default="Desactivado")
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    obra = models.ForeignKey(
        Obra, on_delete=models.PROTECT, related_name="pedidos_obra"
    )

    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="pedidos_cliente"
    )

    planta = models.ForeignKey(
        Planta, on_delete=models.PROTECT, related_name="pedidos_planta"
    )


    def __str__(self):
        return f"{self.tipo} cliente:{self.cliente.nombre} obra:{self.obra.nombre} planta:{self.planta.nombre} "