from django.contrib.gis import admin
from .models import WorldBorder

#admin.site.register(WorldBorder, admin.ModelAdmin)
#admin.site.register(WorldBorder, admin.GISModelAdmin)
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
