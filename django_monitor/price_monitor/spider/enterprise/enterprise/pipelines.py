# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import collections


class EnterprisePipeline(object):
    def __init__(self):
        # self.db_access = pipelines_db.DbAccess()
        self.files = collections.defaultdict(str)
        
    def process_item(self, item, spider):
        ''' Save dict in json format.
        '''
        if self.is_valid(item):
            filename = item['search_time'].replace(' ', '.')
            self.files[filename] += '%s\n'%json.dumps(item)

    def is_valid(self, item):
        '''Check if contains all the required elements.
        '''
        return True
        
    def __del__(self):
        for filename in self.files:
            with open('data/staging/%s'%filename, 'w') as fp:
                fp.write(self.files[filename])
            with open('data/warehouse/%s'%filename, 'w') as fp:
                fp.write(self.files[filename])