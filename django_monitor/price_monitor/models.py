from __future__ import unicode_literals

from django.db import models

class SiteQuery(models.Model):
    search_time = models.CharField(max_length=50)
    search_criteria = models.CharField(max_length=50)
    start_date = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    optional_code = models.CharField(max_length=10)
    site_id = models.ForeignKey('Site', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('search_time', 'site_id')
        
class Site(models.Model):
    site_location = models.CharField(max_length=200)

class Price(models.Model):
    site_query = models.ForeignKey('SiteQuery', on_delete=models.CASCADE)
    car_class = models.CharField(max_length=15)
    car_price = models.DecimalField(max_digits=5, decimal_places=2)
    car_total_price = models.DecimalField(max_digits=5, decimal_places=2)