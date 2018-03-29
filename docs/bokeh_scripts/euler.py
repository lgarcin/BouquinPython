import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import CustomJS, Slider, ColumnDataSource, Range1d
from bokeh.layouts import column

f = lambda x: np.exp(np.sin(x))
F = lambda t, y: np.cos(t) * y
a, b = 0, 10
x = np.linspace(a, b, 1000)
y = f(x)
xx = [0]
yy = [1]
nb = 20
step = (b - a) / nb
for _ in range(nb):
    yy.append(yy[-1] + F(xx[-1], yy[-1]) * step)
    xx.append(xx[-1] + step)

source = ColumnDataSource(dict(x=xx, y=yy))

p = figure(title="Méthode d'Euler", plot_width=700, plot_height=500)
p.x_range = Range1d(a, b)
p.y_range = Range1d(0, 3)
p.title.align = 'center'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.line(x, y, line_width=2, color='blue')
p.line(x='x', y='y', source=source, color='orange', alpha=.5)
slider = Slider(start=20, end=1000, value=20, step=1, title="Nombre")

slider.callback = CustomJS(args=dict(source=source, slider=slider), code="""
    F = (t, y) => Math.cos(t) * y;
    var a = 0;
    var b = 10;
    var data = source.data;
    data.x = new Array();
    data.y = new Array();
    var x = 0
    var y = 1;
    data.x.push(x);
    data.y.push(y);
    var step = (b-a)/slider.value;
    for (var k=0; k<slider.value; k++){
        y += F(x, y) * step;
        x += step;
        data.x.push(x);
        data.y.push(y);
    }
    source.change.emit();
""")

show(column(p, slider))
