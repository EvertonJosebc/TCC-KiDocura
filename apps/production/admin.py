from django.contrib import admin
from .models import Fruta, Compra, Producao, Entrega

# Register your models here.

admin.site.register(Fruta)
admin.site.register(Compra)
admin.site.register(Producao)
admin.site.register(Entrega)