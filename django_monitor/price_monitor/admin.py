from django.contrib import admin
from .models import Site, Price, SiteQuery

admin.site.register(Site)
admin.site.register(SiteQuery)
admin.site.register(Price)