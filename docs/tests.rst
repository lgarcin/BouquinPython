=====
Tests
=====

Un test permet d'effectuer un bloc d'instructions lorsqu'une condition est remplie. On emploie pour cela le mot-clé :code:`if` suivie d'une expression à valeur booléenne.

.. ipython:: python

    a = 4       # Changer la valeur de a pour comprendre ce qui se passe
    if a % 2 ==0 :
        print('a est pair')


Si on veut introduire un bloc d'instructions à exécuter lorsque la condition **n'est pas** remplie, on emploie le mot-clé :code:`else`.

.. ipython:: python

    a = 5
    if a % 2 == 0:
        print('a est pair')\
    else:
        print('a est impair')


Si on veut envisager plusieurs tests successifs, on emploie le mot-clé :code:`elif` (conctraction de :code:`else if`).

.. ipython:: python

    a = 5
    if a % 2 == 0:
        print('a est pair')\
    elif a > 3:
        print('a est impair et strictement supérieur à 3')

On peut évidemment combiner :code:`if`, :code:`elif` et :code:`else`.

.. ipython:: python

    a = 1
    if a % 2 == 0:
        print('a est pair')\
    elif a > 3:
        print('a est impair et strictement supérieur à 3')
    else:
        print('a est impair et inférieur ou égal à 3')

.. note::

    Python dispose

    .. ipython:: python

        2 if 3 < 4 else 3
