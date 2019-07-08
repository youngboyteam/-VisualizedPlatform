from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from helper import make_bokeh_helper
import logging

class UserLogin:
    def login(self):
        logger = logging.getLogger('log')
        logger.info('请求成功！ response_code:{}；response_content:{}'.format(200, 'Hello world !'))
        return render(self,'circle.html')

    def make_circle(self):
       script,div = make_bokeh_helper.make_circle(self)
       return render(self, 'circle.html', {'script': script, 'div': div})