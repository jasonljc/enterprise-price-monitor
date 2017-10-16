from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Site


def index(request):
    site_list = Site.objects.all()
    template = loader.get_template('monitor/index.html')
    context = {
        'site_list': site_list,
    }
    return HttpResponse(template.render(context, request))

def date(request, sample_date):
    
    return HttpResponse('The samples on %s'%sample_date)
    
def date_site(request, sample_date, sample_site):
    return HttpResponse('The samples on %s from %s'%sample_date)