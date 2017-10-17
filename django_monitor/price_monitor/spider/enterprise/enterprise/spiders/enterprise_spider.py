import re
import logging
import json
import scrapy
from datetime import datetime

# from scrapy.selector import Selector
# from scrapy.spiders import Spider
# from scrapy.http.cookies import CookieJar

class EnterpriseSpider(scrapy.Spider):
    name = 'enterprise'
    
    def __init__(self):
        self.start_url = 'https://legacy.enterprise.com/car_rental/home.do'
        self.query_info = {
            'searchCriteria':'10001',
            'startDateMonth':'201710',
            'startDateInput':'31',
            'startDateTime':'1600',
            'endDateMonth':'201711',
            'endDateInput':'1',
            'endDateTime':'1600',
            'optionalCode':'',
        }
        self.query_time = self.get_cur_time()
    
    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.time_selection)
            
    def time_selection(self, response):
        yield scrapy.FormRequest(self.start_url, formdata=self.prepare_form(),
            callback=self.parse_loc_selection)
        
    def parse_loc_selection(self, response):
        ''' Find href links in location selection page
        '''
        # print response.text.encode('utf8')
        regex = re.compile(r'transactionId=WebTransaction1&selectedLocationId=')
        targets = filter(regex.search, response.css('a::attr(href)').extract())
        
        for target in targets:
            logging.info('Finding car info at %s'%response.urljoin(target))
            yield scrapy.Request(response.urljoin(target), callback=self.parse_car_list)
            
    def parse_car_list(self, response):
        # print response.text.encode('utf8')
        # I don't know why tbody has to be left out
        # Get location
        cur_info = self.query_info
        location = self.extract_loc(response)
        if not location:
            logging.info('Cannot find location')
            print response.text.encode('utf8')
        cur_info['location'] = location
        cur_info['query_time'] = self.query_time
        for price_info in self.extract_price(response):
            cur_info.update(price_info)
            print cur_info
    
    def get_cur_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def extract_loc(self, response):
        left_bar = response.css('[id=lss] > table')
        for table in left_bar:
            if (table.css('[id=lochead]')
                and table.css('[id=lochead]').re('Pick Up Location')):
                loc_selector = table.css('table > tr > td[valign=top]')
                loc = ' '.join(loc_selector.css('p').re(r'(\S.*)<br>')[:2])
                logging.info('location is %s'%loc)
                return loc
        return None
                
    def extract_price(self, response):
        table_rows = response.css(
            'div#bodyContent > table > tr[valign=top] > td[valign=top] > table '
            'tr')
        for table_row in table_rows:
            car_info = self.extract_car_list(table_row)
            if car_info:
                yield car_info
                
    def extract_car_list(self, row):
        ''' Get car price information from row selectors.
        '''
        if not row.css('[id=tdCCTotalPrice]'):
            return None
        car_class = row.css('td[valign=middle] > span.normTextBold').re(r'(\S.*)<br>')[0]
        car_price = row.css('[id=tdCCCarPrice]').re(r'\$ (.*) USD')[0]
        car_total_price = row.css('[id=tdCCTotalPrice]').re(r'\$ (.*) USD')[0]
        return {'car_class':car_class, 'car_price': car_price, 'car_total_price':car_total_price}
    
    def prepare_form(self):
        form_dict = {
            'actionPath':'/home',
            'transactionId':'WebTransaction1',
            'hiddenSearchCriteria':'',
            'hiddenAltSearchCriteria':'',
            'hiddenCurrentCountry':'',
            'country':'US',
            'fbo':'',
            'searchCriteria':'10001',
            'returnLocation':'',
            'startDateMonth':'201710',
            'startDateInput':'31',
            'startDateTime':'1600',
            'endDateMonth':'201711',
            'endDateInput':'1',
            'endDateTime':'1600',
            'carClassDrop':'',
            'ageDrop':'25',
            'search':'Search',
            'optionalCode':'',
        }
        form_dict.update(self.query_info)
        return form_dict