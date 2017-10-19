from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Site

from spider import data_loader


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
    
def request_add(request):
    input_time = request.GET.get('input_time')
    if input_time:
        loader = data_loader.DataLoader()
        loader.check_staging()
    return render(request, 'monitor/add.html')