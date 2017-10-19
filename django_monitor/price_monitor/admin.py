from django.contrib import admin
from .models import Site, Price, SiteQuery

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_location',)
    
class SiteQueryAdmin(admin.ModelAdmin):
    list_display = ('search_time','search_criteria','start_date','start_time',
                    'end_date','end_time','optional_code','site_id')
                    
class PriceAdmin(admin.ModelAdmin):
    list_display = ('site_query','car_class','car_price','car_total_price')

admin.site.register(Site, SiteAdmin)
admin.site.register(SiteQuery, SiteQueryAdmin)
admin.site.register(Price, PriceAdmin)