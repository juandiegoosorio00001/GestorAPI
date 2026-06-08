from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(default=0)
    
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos'
    )

    creado = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre