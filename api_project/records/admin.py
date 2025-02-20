# Register your models here.
from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_document', 'institution', 'date', 'paid', 'provider')
    search_fields = ('name', 'institution', 'provider')
    list_filter = ('type_of_document', 'paid')
