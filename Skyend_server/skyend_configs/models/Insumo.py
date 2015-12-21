from django.db import models
from .UnidadMedida import UnidadMedida
from .Categoria import Categoria
from ..enums import ESTADO_CHOICES, ACT


class Insumo(models.Model):

    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=60)
    unidad_medida = models.ForeignKey(UnidadMedida, null=True, blank=True)

    categoria = models.ManyToManyField(  # , through='ModuleGroup'
        Categoria, related_name='insumo_set', null=True, blank=True)

    estado = models.CharField(
        max_length=50, choices=ESTADO_CHOICES, default=ACT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"

    def __str__(self):
        return self.nombre
