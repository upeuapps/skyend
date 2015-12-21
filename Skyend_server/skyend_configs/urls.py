from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views.NaturalPersonView import NaturalPersonViewSet
from .views.UnidadMedidaView import UnidadMedidaViewSet
from .views.InsumoView import InsumoViewSet
from .views.CategoriaView import CategoriaViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'categorias', CategoriaViewSet)

router.register(r'insumos', InsumoViewSet)

router.register(r'unidadmedidas', UnidadMedidaViewSet)

router.register(r'naturalpersons', NaturalPersonViewSet)


urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),

)
