# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pipelines_db


class EnterprisePipeline(object):
    def __init__(self):
        # self.db_access = pipelines_db.DbAccess()
        pass
        
    def process_item(self, item, spider):
        if self.is_valid(item):
            return item

    def is_valid(self, item):
        '''Check if contains all the required elements.
        '''
        return True