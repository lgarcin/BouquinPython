import numpy as np
from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import CustomJS, Slider, Span, Label
from bokeh.layouts import column, widgetbox

f = np.sin

a, b, N = 2, 4, 10
c = (a + b) / 2

x = np.linspace(a, b, 500)
y = f(x)

la, lb, lc = [a], [b], [c]
for _ in range(N + 1):
    if f(a) * f(c) <= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2
    la.append(a)
    lb.append(b)
    lc.append(c)

source = ColumnDataSource(data=dict(la=la, lb=lb, lc=lc))

p = figure(title="Résolution par dichotomie", plot_width=700, plot_height=500)
p.title.align = 'center'
p.line(x, y, line_width=2)

slider = Slider(start=0, end=N, value=0, step=1, title="Itérations")
spa = Span(location=la[slider.value], dimension='height',
           line_color='red', line_dash='dashed', line_width=3)
p.add_layout(spa)
spb = Span(location=lb[slider.value], dimension='height',
           line_color='green', line_dash='dashed', line_width=3)
p.add_layout(spb)
spc = Span(location=lc[slider.value], dimension='height',
           line_color='orange', line_dash='dashed', line_width=3)
p.add_layout(spc)

slider.callback = CustomJS(args=dict(spa=spa, spb=spb, spc=spc, source=source, slider=slider), code="""
    var n = slider.value;
    spa.location = source.data['la'][n];
    spb.location = source.data['lb'][n];
    spc.location = source.data['lc'][n];
""")

show(column(p, widgetbox(slider)))
