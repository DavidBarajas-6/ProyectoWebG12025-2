from django.contrib import admin
from .models import Plan, Tipo, Comida, Menu

# Registrar Tipo
@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registrar Comida
@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ('name', 'calorias')
    search_fields = ('name',)

# Registrar Plan
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'tipo', 'realizado', 'created_at')
    list_filter = ('realizado', 'tipo', 'created_at')
    search_fields = ('title', 'content')

# Registrar Menu
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('plan', 'comida', 'cantidad', 'get_calorias_totales')

    def get_calorias_totales(self, obj):
        return obj.calorias_totales

    get_calorias_totales.short_description = 'Calorías totales'

