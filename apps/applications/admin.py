from django.contrib import admin
from .models import Zayavka


@admin.register(Zayavka)
class ZayavkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'polzovatel', 'kurs', 'data_nachala', 'oplata', 'status', 'sozdan')
    list_editable = ('status',)
    list_filter = ('status', 'kurs')
    search_fields = ('polzovatel__username', 'kurs')
