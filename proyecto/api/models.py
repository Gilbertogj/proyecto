from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Cliente model."""
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    rfc = models.TextField(max_length=100, unique=True)
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
    telefono = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.nombre} {self.residente}"


class Planta(models.Model):
    """Planta model."""
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(max_length=1000)
    telefono = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"


class Pedido(models.Model):
    """Cliente model."""

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
    tipo = models.CharField(max_length=30, choices=TIPO_CONCRETO, default="C")

    RESISTENCIA = (
        ("100", "100"),
        ("200", "200"),
        ("250", "250"),
        ("300", "300"),
        ("350", "350"),
        ("400", "400"),
        ("650", "650"),
    )
    resistencia = models.CharField(max_length=10, choices=RESISTENCIA, default="200")

    EDAD = (
        ("R01", "R01"),
        ("R03", "R03"),
        ("R07", "R07"),
        ("R14", "R14"),
        ("N", "N"),
    )
    edad = models.CharField(max_length=10, choices=EDAD, default="N")

    TAMAÑO_NOMINAL= (
        ("10", "3/8 10mm"),
        ("20", "3/4 20mm"),
        ("40", "1 1/12 40mm"),
        ("05", "Arena"),
    )
    tma = models.CharField(max_length=20, choices=TAMAÑO_NOMINAL, default="20")

    REVENIMIENTO= (
        ("06", "06 cm"),
        ("08", "08 cm"),
        ("10", "10 cm"),
        ("12", "12 cm"),
        ("14", "14 cm"),
        ("16", "16 cm"),
        ("18", "18 cm"),
        ("22", "20 cm"),
    )
    revenimiento = models.CharField(max_length=20, choices=REVENIMIENTO, default="14")

    FORMA= (
        ("T", "Tirado"),
        ("B", "Bombeado"),
    )
    forma = models.CharField(max_length=10, choices=FORMA, default="14")
    
    TIPO_BOMBA= (
        ("Pluma", "Bomba Pluma"),
        ("Estacionaria", "Bomba Estacionaria"),
    )
    tipo_bomba = models.CharField(max_length=10, choices=TIPO_BOMBA, default="Pluma")

    numero_bomba = models.CharField(max_length=255)
    metros_adicionales = models.CharField(max_length=255)
    aditivo = models.CharField(max_length=255)

    ELEMENTO_COLAR= (
        ("Ban", "Bomba Pluma"),
        ("Estacionaria", "Bomba Estacionaria"),
    )

    elemento_colar = models.CharField(max_length=10, choices=TIPO_BOMBA, default="Pluma")
    observaciones = models.CharField(max_length=255)



    fecha_pedido = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.alias}"