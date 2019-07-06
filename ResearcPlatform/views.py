from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

class UserLogin:
    def login(self):
        logger = logging.getLogger('log')
        logger.info('请求成功！ response_code:{}；response_content:{}'.format(200, 'Hello world !'))
        return HttpResponse("Hello world ! ")