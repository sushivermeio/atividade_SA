from django.contrib import admin
from galeria.models import RegistroLogin


@admin.register(RegistroLogin)
class RegistroLoginAdmin(admin.ModelAdmin):
    list_display = ('user', 'horario_entrada', 'horario_saida')