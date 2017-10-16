from util import ProbeUtil

url1 = 'https://legacy.enterprise.com/car_rental/home.do'
url2 = 'https://legacy.enterprise.com/car_rental/location.do?transactionId=WebTransaction6&selectedLocationId=323C'

probe_util = ProbeUtil()

form_dict = {
        'actionPath':'/home',
        'transactionId':'WebTransaction1',
        'hiddenSearchCriteria':'',
        'hiddenAltSearchCriteria':'',
        'hiddenCurrentCountry':'',
        'country':'US',
        'fbo':'',
        'searchCriteria':'90007',
        'returnLocation':'',
        'startDateMonth':'201710',
        'startDateInput':'18',
        'startDateTime':'1200',
        'endDateMonth':'201710',
        'endDateInput':'19',
        'endDateTime':'1200',
        'carClassDrop':'',
        'ageDrop':'25',
        'search':'Search',
        'optionalCode':'',
    }   
response1 = probe_util.open_url(url1)    
# response2 = probe_util.open_url(url1, form_dict)
response3 = probe_util.open_url(url2)
print response3.read()