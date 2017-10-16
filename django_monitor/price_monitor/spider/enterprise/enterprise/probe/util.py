import urllib2
import urllib
import cookielib

class ProbeUtil(object):
    
    def __init__(self, cookies=None, cookie_filename='cookie.txt'):
        self.opener = None
        self.cookie_filename = cookie_filename
        self.cookies = cookies
        if not self.cookies:
            self.default_init()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(cookies))
            
    def default_init(self):
        ''' Default action for starting a opener with a session
        '''
        # default_url = 'https://legacy.enterprise.com/car_rental/home.do'
        self.cookies = cookielib.MozillaCookieJar(self.cookie_filename)
            
    def open_url(self, url, data=None):
        ''' Open target url and return response
        
        Args:
            url: (string)
            data: (dict)
        '''
        response = None
        if data:
            form_data = urllib.urlencode(data)
            request = urllib2.Request(url, form_data)
            response = self.opener.open(request)
        else:
            response = self.opener.open(url)
        self.cookies.save(ignore_discard=True, ignore_expires=True)
        return response