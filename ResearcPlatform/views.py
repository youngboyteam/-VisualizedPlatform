from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import numpy as np
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure
import logging

class UserLogin:
    def login(self):
        logger = logging.getLogger('log')
        logger.info('请求成功！ response_code:{}；response_content:{}'.format(200, 'Hello world !'))
        return render(self,'circle.html')

    def make_circle(request):
        p = figure(plot_width=400, plot_height=400)
        # 方框
        p.square(np.random.randint(1, 10, 5), np.random.randint(1, 10, 5), size=20, color="navy")
        # 圆形
        p.circle(np.random.randint(1, 10, 5), np.random.randint(1, 10, 5), size=10, color="green")

        script, div = components(p, CDN)

        return render(request, 'circle.html', {'script': script, 'div': div})