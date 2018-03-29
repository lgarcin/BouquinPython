import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import CustomJS, Slider, RadioButtonGroup, ColumnDataSource
from bokeh.layouts import widgetbox, column

f = np.cos
a, b = 0, np.pi
x = np.linspace(a, b, 1000)
xx = np.linspace(a, b, 10)
y = f(x)
yy = f(xx)

xpatches = [[xx[i], xx[i+1], xx[i+1], xx[i]] for i in range(len(xx)-1)]
ypatches = [[0, 0, yy[i+1], yy[i]] for i in range(len(yy)-1)]
source = ColumnDataSource(dict(xpatches=xpatches, ypatches=ypatches))

p = figure(title="Méthode des trapèzes", plot_width=700, plot_height=500)
p.title.align = 'center'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.line(x, y, line_width=2, color='blue')
p.patches(xs='xpatches', ys='ypatches', source=source, color='orange', alpha=.5)
slider = Slider(start=10, end=100, value=10, step=1, title="Nombre")

slider.callback = CustomJS(args=dict(source=source, slider=slider), code="""
    var a = 0;
    var b = Math.PI;
    var data = source.data;
    var f = Math.cos;
    data.xpatches = new Array();
    data.ypatches = new Array();
    var x = a;
    var y = f(a);
    var step = (b-a)/slider.value;
    for (var k=0; k<slider.value; k++){
        var xx = x+step;
        var yy = f(xx);
        data.xpatches.push([x, xx, xx, x]);
        data.ypatches.push([0, 0, yy, y]);
        x = xx;
        y = yy;
    }
    source.change.emit();
""")

show(column(p, widgetbox(slider)))
