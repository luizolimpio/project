# django imports
from django.contrib import admin

# lfs imports
from lfs.core.models import Action
from lfs.core.models import ActionGroup
from lfs.core.models import Shop
from lfs.core.models import Country
from lfs.core.models import Estado,Cidade

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class Estadomodeladmin(admin.ModelAdmin):
    inlines = [CidadeInline]


admin.site.register(Estado,Estadomodeladmin)
admin.site.register(Shop)
admin.site.register(Action)
admin.site.register(ActionGroup)
admin.site.register(Country)
