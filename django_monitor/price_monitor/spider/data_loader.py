from price_monitor.models import Site, Price, SiteQuery
import json
from os import path
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)


class DataLoader(object):
    def __init__(self):
        self.staging_path = 'price_monitor/spider/enterprise/data/staging'
    
    def check_staging(self):
        '''Load files from staging path if there is any
        '''
        file_list = os.listdir(self.staging_path)
        if not file_list:
            logger.info('No file found in staging path %s'%self.staging_path)
        else:
            for basename in file_list:
                file_path = path.join(self.staging_path, basename)
                logger.info('Loading file %s'%file_path)
                self.load_from_staging(file_path)
    
    def load_from_staging(self, file_path):
        with open(file_path) as fp:
            lines = fp.read().split('\n')
            for line in lines:
                if line:
                    self.load_line(line)
                    
    def load_line(self, line):
        def build_site(d):
            site_set = Site.objects.filter(site_location=d['location'])
            if not site_set:
                logger.info('Saving new location %s'%d['location'])
                site = Site(site_location=d['location'])
                site.save()
            return Site.objects.get(site_location=d['location'])
            
        def build_site_query(d, site):
            
            site_query_set = SiteQuery.objects.filter(search_time=d['search_time'], site_id=site)
            if not site_query_set:
                start_date = '%s%s'%(d['start_date_month'], d['start_date_input'].zfill(2))
                end_date = '%s%s'%(d['end_date_month'], d['end_date_input'].zfill(2))
                site_query = SiteQuery(search_time=d['search_time'],
                                       search_criteria=d['search_criteria'],
                                       start_date=start_date,
                                       start_time=d['start_date_time'],
                                       end_date=end_date,
                                       end_time=d['end_date_time'],
                                       optional_code=d['optional_code'],
                                       site_id=site)
                site_query.save()
            return SiteQuery.objects.get(search_time=d['search_time'], site_id=site)
            
        def build_price(d, site_query):
            price = Price(site_query=site_query,
                          car_class=d['car_class'],
                          car_price=d['car_price'],
                          car_total_price=d['car_total_price'])
            price.save()
        d_ = json.loads(line)
        # Save Site
        site_ = build_site(d_)
        # Save SiteQuery
        site_query_ = build_site_query(d_, site_)
        # Save Price
        build_price(d_, site_query_)