=================
Analyse numérique
=================


Statistiques
============


Le programme stipule que les étudiants doivent savoir calculer les éléments statistiques simples d'une liste de nombres : **moyenne** et **variance**.

Le calcul de la moyenne est on ne peut plus simple : il s'agit de la somme des éléments de la liste divisée par le nombre d'éléments de cette liste. De manière plus formmelle, la moyenne :math:`m` d'une liste :math:`(x_1,\dots,x_n)` de nombres est

.. math::

    m=\frac{1}{n}\sum_{k=1}^nx_k

.. ipython:: python

    def moyenne(liste):
        somme = 0
        for el in liste:
            somme += el
        return somme / len(liste)

    moyenne([1, 2, 3])

Evidemment, Python dispose déjà deux fonctions permettant de calculer aisément la moyenne d'une liste de nombres. On peut par exemple utiliser la fonction :code:`sum` qui, comme son nom l'indique, calcule la somme des éléments d'une liste (ou plus généralement d'un objet de type itérable).

.. ipython:: python

    moyenne = lambda liste: sum(liste) / len(liste)

    moyenne([1, 2, 3])

Le module :code:`numpy` dispose même d'une fonction :code:`mean` (*moyenne* en anglais).

.. ipython:: python

    from numpy import mean

    mean([1, 2, 3])


On peut donner deux expressions de la variance :math:`v` d'une liste :math:`(x_1,\dots,x_n)` de nombres dont on dispose déjà de la moyenne :math:`m`.

.. math::

    v = \left(\frac{1}{n}\sum_{k=1}^nx_k^2\right)-m^2 = \frac{1}{n}\sum_{k=1}^n(x_k-m)^2


En utilisant la première expression, on peut par exemple donner cette fonction de calcul de la variance.

.. ipython:: python

    def variance(liste):
        s1, s2 = 0, 0
        n = len(liste)
        for el in liste:
            s1 += el
            s2 += el * el
        return s2 / n - (s1 / n) ** 2

    variance([1, 2, 3])

On peut également utiliser une des fonctions de calcul de moyenne définies précédemment.

.. ipython:: python

    variance = lambda liste: moyenne([el ** 2 for el in liste]) - moyenne(liste) ** 2

    variance([1, 2, 3])

Si l'on préfère, on peut également utiliser la deuxième expression de la variance.

.. ipython:: python

    def variance(liste):
        m = moyenne(liste)
        return moyenne([(el - m) ** 2 for el in liste])

    variance([1, 2, 3])

Bien entendu, le module :code:`numpy` dipose déjà d'une fonction ad hoc : la fonction :code:`var`.

.. ipython:: python

    from numpy import var

    var([1, 2, 3])


Résolution d'équations par dichotomie
=====================================

On suppose qu'on dispose d'une fonction :math:`f` continue et strictement monotone sur un intervale :math:`[a,b]` vérifiant :math:`f(a)f(b)\leq0`. Le théorème des valeurs intermédiaires garantit l'existence d'une unique solution à l'équation :math:`f(x)=0` sur l'intervalle :math:`[a,b]`. Pour obtenir une valeur approchée de cette solution, on procède par **dichotomie** :

    1. On calcule :math:`c=(a+b)/2` et :math:`f(c)`.
    2. Si :math:`f(a)f(c)\leq0`, la solution appartient à l'intervalle :math:`[a,c]`. Sinon, elle appartient à l'intervalle :math:`[c,b]`.
    3. Dans le premier cas, on remplace :math:`b` par :math:`c` tandis que dans le second cas, on remplace :math:`a` par :math:`c`.
    4. On répète les étapes 1., 2. et 3. tant que la longeur de l'intervalle :math:`[a,b]` est supérieur à une précision :math:`\epsilon` donnée.
    5. La valeur de :math:`c` est alors une valeur appochée de la solution de :math:`f(x)=0` à :math:`\epsilon/2` près.


.. bokeh-plot::
    :source-position: none

    import numpy as np

    from bokeh.plotting import figure, show, ColumnDataSource
    from bokeh.models import CustomJS, Slider, Span, Label
    from bokeh.layouts import column, widgetbox

    f = np.sin

    a, b, N = 2, 4, 10
    c = (a+b) / 2

    x = np.linspace(a, b, 500)
    y = f(x)

    la, lb, lc = [a], [b], [c]
    for _ in range(N+1):
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
    spa = Span(location=la[slider.value], dimension='height', line_color='red', line_dash='dashed', line_width=3)
    p.add_layout(spa)
    spb = Span(location=lb[slider.value], dimension='height', line_color='green', line_dash='dashed', line_width=3)
    p.add_layout(spb)
    spc = Span(location=lc[slider.value], dimension='height', line_color='orange', line_dash='dashed', line_width=3)
    p.add_layout(spc)

    slider.callback = CustomJS(args=dict(spa=spa, spb=spb, spc=spc, source=source, slider=slider), code="""
        var n = slider.value;
        spa.location = source.data['la'][n];
        spb.location = source.data['lb'][n];
        spc.location = source.data['lc'][n];
    """)

    show(column(p, widgetbox(slider)))

.. ipython:: python

    def dicho(f, a, b, eps):
        while abs(b-a) > eps:
            c = (a + b) / 2
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
        return (a+b) / 2

    from math import sin
    dicho(sin, 2, 4, .0001)


Calcul d'intégrales
===================

Méthode des rectangles
----------------------

On peut approcher une intégrale par une somme d'aire de rectangles comme l'indique la figure suivante.

.. bokeh-plot::
    :source-position: none

    import numpy as np
    from bokeh.plotting import figure, show
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

Plus précisément, en posant :math:`x_k=a+k(b-a)/n` où :math:`n` désigne le nombre de rectangles :

.. math::

    \begin{align*}
    R_n&=\frac{b-a}{n}\sum_{k=0}^{n-1}f(x_k)\approx\int_a^bf(t)\,\mathrm{dt}&\text{(rectangles verts)}\\
    S_n&=\frac{b-a}{n}\sum_{k=1}^nf(x_k)\approx\int_a^bf(t)\,\mathrm{dt}&\text{(rectangles rouges)}
    \end{align*}

On peut alors proposer la fonction suivante pour approcher l'intégrale d'une fonction :math:`f` sur un intervalle :math:`[a,b]`.

.. ipython:: python

    def rectangles(f, a, b, N, side):
        pas = (b-a) / N
        x = a
        somme = 0
        for _ in range(N):
            if side:
                somme += f(x)
            x += pas
            if not side:
                somme += f(x)
        return somme / N

    rectangles(lambda x: x**2, 0, 1, 100, True)
    rectangles(lambda x: x**2, 0, 1, 100, False)

Les sommes :math:`R_n` et :math:`S_n` sont appelées des *sommes de Riemann* et on peut même prouver que pour des fonctions :math:`f` continues,

.. math::
    \lim_{n\to+\infty}S_n=\lim_{n\to+\infty}T_n=\int_a^bf(t)\,\mathrm{dt}

En particulier, l'appoximation de l'intégrale :math:`\int_a^bf(t)\,\mathrm{dt}` est d'autant meilleure que le nombre :math:`n` de rectangles est grand, ce qui se conçoit très bien géométriquement.


Méthode des trapèzes
--------------------

On peut également apporcher une intégrale comme une somme d'aires de trapèzes comme sur la figure suivante. Bien évidemment, l'approximation de l'intégrale est meilleure qu'avec des ractangles.

.. bokeh-plot::
    :source-position: none

    import numpy as np
    from bokeh.plotting import figure, show
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
    show(column(p, widgetbox(slider)))

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

A nouveau, en posant :math:`x_k=a+k(b-a)/n` où :math:`n` désigne le nombre de trapèzes :

.. math::

    T_n=\frac{b-a}{n}\sum_{k=0}^{n-1}\frac{f(x_k)+f(x_{k+1})}{2}\approx\int_a^bf(t)\,\mathrm{dt}\\

On peut évidemment remarquer que :math:`T_n=(R_n+S_n)/2`. En fait, la somme précédente peut se réécrire de manière différente :

.. math::

    T_n=\frac{b-a}{n}\left(\frac{f(a)+f(b)}{2}+\sum_{k=1}^{n-1}f(x_k)\right)

Cette nouvelle formule permet de calculer :math:`T_n` en effectuant moins d'opérations qu'avec la formule précédente. On peut alors donner l'algorithme suivant.

.. ipython:: python

    def trapezes(f, a, b, N):
        pas = (b-a) / N
        x = a
        somme = (f(a) + f(b)) / 2
        for _ in range(N-1):
            x += pas
            somme += f(x)
        return somme / N

    trapezes(lambda x: x**2, 0, 1, 100)


.. todo:: Méthodes de quadrature
.. todo:: parler de quad dans scipy
.. todo:: augmenter n très bien mais pb d'arrondi qaund n grand

Résolution d'équations différentielles
======================================

L'objectif est de résoudre numériquement des équations différentielles : c'est-à-dire qu'on ne cherche pas des expressions explicites des solutions mais des valeurs approchées.

Pour commencer, on traitera le cas de *problème de Cauchy* d'ordre 1.

.. math::

    \left\{
    \begin{aligned}
    y'&=f(t,y)\\
    y(t_0)&=y_0
    \end{aligned}
    \right.


On rappelle qu'un tel problème consiste en la donnée d'une équation différentielle résolue d'ordre 1 :math:`y'=f(t,y)` et d'une condition initiale :math:`y(t_0)=y_0`. Le théorème de Cauchy-Lipschitz garantit l'existence et l'unicité d'une solution à ce problème lorsque :math:`f` est suffisamment règulière.

L'idée est d'utiliser une approximation affine de la fonction solution : :math:`y(t+\Delta\!t)\approx y(t)+y'(t)\Delta\!t`. Le calcul de :math:`y'(t)` est possible grâce à l'équation différentielle si l'on connaît :math:`y(t)` puisque :math:`y'(t)=f(t,y(t))`. On itère ce processus pour calculer des valeurs approchées à des intervalles de temps réguliers. Plus précisément, en posant :math:`t_k=t_0+k\Delta\!t`, on a alors

.. math::

    \begin{alignat}{2}
    y(t_1) & \approx y(t_0)+y'(t_0)\Delta\!t & = y(t_0)+f(t_0,y_0)\Delta\!t &= y_1\\
    y(t_2) & \approx y(t_1)+y'(t_1)\Delta\!t & \approx y(t_1)+f(t_1,y_1)\Delta\!t &= y_2\\
    y(t_3) & \approx y(t_2)+y'(t_2)\Delta\!t & \approx y(t_2)+f(t_2,y_2)\Delta\!t &= y_3\\
    \dots
    \end{alignat}

La méthode que l'on vient de décrire porte le nom de **méthode d'Euler**.

.. ipython:: python

    def euler(f, t0, y0, pas, nb):
        t = t0
        y = y0
        liste_t = [t]
        liste_y = [y]
        for _ in range(nb):
            y += f(t, y) * pas
            t += pas
            liste_t.append(t)
            liste_y.append(y)
        return liste_t, liste_y

Par exemple, on calcule ici une solution approchée au système de Cauchy

.. math::

    \left\{
    \begin{aligned}
    y'&=\cos(t)y\\
    y(0)&=1
    \end{aligned}
    \right.

.. ipython:: python

    from math import cos
    f = lambda t, y: cos(t) * y
    liste_t, liste_y = euler(f, 0, 1, .01, 1000)

On peut tracer la courbe de la solution apporchée que l'on peut comparer à la courbe de la solution exacte. En effet, on montre sans peine que l'unique solution de cd problème de Cauchy est la fonction :math:`x\mapsto e^{\sin(x)}`.

.. ipython:: python

    import matplotlib.pyplot as plt
    from numpy import exp, sin, linspace

    # Tracé de la solution approchée
    plt.plot(liste_t, liste_y, color='red', label='Solution approchée');

    # Tracé de la solution exacte
    x = linspace(0, 10, 1000)
    y = exp(sin(x))
    plt.plot(x, y, color='blue', label='Solution exacte');

    plt.legend();

    @suppress
    plt.savefig('_build/html/_images/euler.png', width=10)
    plt.show()

.. image:: ./_images/euler.png



Bien entendu, l'approximation affine :math:`y'(t+\Delta\!t)\approx f(t)+f'(t)\Delta\!t` est d'autant meilleur que :math:`\Delta\!t` est petit.

.. bokeh-plot::
    :source-position: none

    import numpy as np
    from bokeh.plotting import figure, show
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
    show(column(p, slider))

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


.. todo:: parler de odeint
