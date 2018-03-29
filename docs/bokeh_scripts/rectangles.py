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

source = ColumnDataSource(dict(xleft=xx[:-1], xright=xx[1:], yleft=yy[1:], yright=yy[:-1], bottom=[0]*9))

p = figure(title='Méthode des rectangles', plot_width=700, plot_height=500)
p.title.align = 'center'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.line(x, y, line_width=2, color='blue')
left = p.quad(left='xleft', right='xright', top='yleft', bottom='bottom', color='red', alpha=.5, source=source)
right = p.quad(left='xleft', right='xright', top='yright', bottom='bottom', color='green', alpha=.5, source=source)
right.visible = False

radio = RadioButtonGroup(labels=['Gauche', 'Droite'], active=0)
slider = Slider(start=10, end=100, value=10, step=1, title='Nombre de rectangles')

radio.callback = CustomJS(args=dict(radio=radio, left=left, right=right), code="""
    switch(radio.active){
        case 0:
            left.visible = true;
            right.visible = false;
            break;
        case 1:
            left.visible = false;
            right.visible = true;
            break;
        default:
            left.visible = true;
            right.visible = true;
        }
""")

slider.callback = CustomJS(args=dict(source=source, slider=slider), code="""
    var a = 0;
    var b = Math.PI;
    var data = source.data;
    var f = Math.cos;
    var x = a;
    var y = f(a);
    var step = (b-a)/slider.value;
    data.xleft = new Array();
    data.xright = new Array();
    data.yleft = new Array();
    data.yright = new Array();
    data.bottom = new Array();
    data.xleft.push(x);
    data.yright.push(y)
    data.bottom.push(0);
    for (var k=0; k<slider.value-1; k++){
        x += step;
        y = f(x);
        data.xleft.push(x);
        data.xright.push(x)
        data.yleft.push(y);
        data.yright.push(y);
        data.bottom.push(0);
    }
    x += step;
    y = f(x);
    data.xright.push(x);
    data.yleft.push(y);
    source.change.emit();
""")

show(column(p, widgetbox(radio, slider)))
