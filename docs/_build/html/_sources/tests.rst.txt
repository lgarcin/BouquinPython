=====
Tests
=====

Un test permet d'effectuer un bloc d'instructions lorsqu'une condition est remplie. On emploie pour cela le mot-clé :code:`if` suivie d'une expression à valeur booléenne.

.. ipython:: python

    a = 5       # Changer la valeur de a pour comprendre ce qui se passe
    x = 0
    if a > 1:
        x = 1
    x


Si on veut introduire un bloc d'instructions à exécuter lorsque la condition **n'est pas** remplie, on emploie le mot-clé :code:`else`.

.. ipython:: python

    a = 5
    x = 0
    if a < 1:
        x = 1
    else:
        x = 2
    x


Si on veut envisager plusieurs tests successifs, on emploie le mot-clé :code:`elif` (conctraction de :code:`else if`).

.. ipython:: python

    a = 5
    x = 0
    if a < 1:
        x = 1
    elif a > 3:
        x = 2
    x

On peut évidemment combiner :code:`if`, :code:`elif` et :code:`else`.

.. ipython:: python

    a = 5
    x = 0
    if a < 1:
        x = 1
    elif a < 2:
        x = 2
    else:
        x = 3
    x
