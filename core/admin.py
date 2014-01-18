from django.contrib import admin
from core.forms import CoordinadorForm
from core.models import Coordinador,LiderGrupo,Estudiante

class CoordinadorAdmin(admin.ModelAdmin):
    add_form = CoordinadorForm
    list_display = ('user.username','codigo','user.first_name','user.last_name')

admin.site.register(Coordinador)
admin.site.register(LiderGrupo)
admin.site.register(Estudiante)