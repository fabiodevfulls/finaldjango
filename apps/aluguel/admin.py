from django.contrib import admin
from apps.aluguel.models import Carro


class ListatandoCarro(admin.ModelAdmin):
    list_display = ['modelo', 'ano', 'publicada']
    list_display_links = ['modelo']
    list_editable = ['publicada']
    list_per_page = 10


admin.site.register(Carro, ListatandoCarro)





