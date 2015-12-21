from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from ..models.UnidadMedida import UnidadMedida
from ..models.Insumo import Insumo

from ..utils import SetPagination
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce
from rest_framework.response import Response

# from .UnidadMedidaView import UnidadMedidaSerializer


class InsumoSerializer(serializers.ModelSerializer):

    um_nombre = serializers.ReadOnlyField(
        source='unidad_medida.nombre')

    # unidad_medida = UnidadMedidaSerializer(
    #    required=False, many=False, read_only=True)

    class Meta:
        model = Insumo
        # fields = ('url', 'abrev', 'descr')


class InsumoViewSet(viewsets.ModelViewSet):  # API REST
    queryset = Insumo.objects.filter()
    serializer_class = InsumoSerializer
    pagination_class = SetPagination
    # paginate_by = 3
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
