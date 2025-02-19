# Register your models here.
from django.contrib import admin
from .models import Recognition

@admin.register(Recognition)
class RecognitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_recognition', 'institution', 'date')
    search_fields = ('name', 'type_of_recognition')
    list_filter = ('name', 'type_of_recognition')