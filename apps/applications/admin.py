from django.contrib import admin
<<<<<<< HEAD
from .models import Zayavka


@admin.register(Zayavka)
class ZayavkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'polzovatel', 'kurs', 'data_nachala', 'oplata', 'status', 'sozdan')
    list_editable = ('status',)
    list_filter = ('status', 'kurs')
    search_fields = ('polzovatel__username', 'kurs')
=======
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'start_date', 'payment_method', 'status', 'created_at')
    list_editable = ('status',)          
    list_filter = ('status', 'course')   
    search_fields = ('user__username', 'course')
# Register your models here.
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
