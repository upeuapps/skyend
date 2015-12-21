from django.contrib import admin
from .models.JerarquiaAcad import JerarquiaAcad
from .models.Institucion import Institucion
from .models.Facultad import Facultad
from .models.Escuela import Escuela
from .models.Carrera import Carrera

from .models.Insumo import Insumo
from .models.Categoria import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")

admin.site.register(Categoria, CategoriaAdmin)


class InsumoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "unidad_medida")

admin.site.register(Insumo, InsumoAdmin)


class JerarquiaAcadAdmin(admin.ModelAdmin):
    list_display = ("tipo", "institucion", "parent")


class InstitucionAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")
    list_per_page = 2


class FacultadAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")


class CarreraAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")


admin.site.register(JerarquiaAcad, JerarquiaAcadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(Carrera, CarreraAdmin)
