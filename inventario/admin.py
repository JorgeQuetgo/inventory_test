from django.contrib import admin
from inventario.utils import load_document

# Register your models here.

from .models import *

# admin.site.register(Inventory)
# admin.site.register(LoadFile)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'stock', 'price')


class LoadFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file', 'created_at', 'jfile')
    exclude = ('jfile',)

    def save_model(self, request, obj, form, change):
        load_document(file=obj.file, object=obj)
        super(LoadFileAdmin, self).save_model(request, obj, form, change)



admin.site.register(Inventory, InventoryAdmin)
admin.site.register(LoadFile, LoadFileAdmin)
