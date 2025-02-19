from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_recognition', 'institution', 'date')
    search_fields = ('name', 'type_of_recognition')
    list_filter = ('institution')