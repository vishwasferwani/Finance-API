from django.contrib import admin
from .models import Record
# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'type', 'category', 'date']
    list_filter = ['type', 'category']
    search_fields = ['category']