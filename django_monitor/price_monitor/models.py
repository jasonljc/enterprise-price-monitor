from __future__ import unicode_literals

from django.db import models

    
class Site(models.Model):
    site_name = models.CharField(max_length=100)
    site_location = models.CharField(max_length=200)

class Price(models.Model):
    car_site = models.ForeignKey('Site', on_delete=models.CASCADE)
    car_tier = models.CharField(max_length=40)
    car_price = models.IntegerField(default=0)
    sample_date = models.DateTimeField(auto_now_add=True, verbose_name=_(
        'Date of the price invoice.'))
    sample_promotion = models.CharField(max_length=10)