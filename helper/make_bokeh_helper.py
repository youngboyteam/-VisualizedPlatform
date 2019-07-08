import numpy as np
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure

def make_circle(self):
    p = figure(plot_width=400, plot_height=400)
    # 方框
    p.square(np.random.randint(1, 10, 5), np.random.randint(1, 10, 5), size=20, color="navy")
    # 圆形
    p.circle(np.random.randint(1, 10, 5), np.random.randint(1, 10, 5), size=10, color="green")

    script, div = components(p, CDN)

    return [script,div]
