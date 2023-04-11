from django.contrib import admin
from . import models


class productAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_filter = ['title', 'prise', 'is_active']
    list_display = ['title', 'prise', 'is_active']
    list_editable = ['is_active']


admin.site.register(models.product, productAdmin)
admin.site.register(models.productCategory)
admin.site.register(models.productinformation)
