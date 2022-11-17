from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class HouseResource(resources.ModelResource):
   class Meta:
      model = House

class HouseAdmin(ImportExportModelAdmin):
   resource_class = HouseResource

admin.site.register(House, HouseAdmin)

class HouseLocationModelAdmin(admin.ModelAdmin):
   list_display = ('id', 'city')
   list_display_links = ('id', 'city')
   ordering = ('id',)

class HouseTypeModelAdmin(admin.ModelAdmin):
   list_display = ('id', 'type_house')
   list_display_links = ('id', 'type_house')
   ordering = ('id',)

admin.site.register(HouseLocation, HouseLocationModelAdmin)
admin.site.register(HouseType, HouseTypeModelAdmin)

