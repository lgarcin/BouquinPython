======
Tuples
======

Un *tuple* est tout à fait similaire à une liste : il s'agit d'une collection d'objets [#tuple]_ . On crée un tuple en séparant les objets par des des virgules :code:`,` et en les encadrant *éventuellement* par des parenthèses :code:`(...)`.

.. ipython:: python

    type((1,2,3))
    a = 1,2,3
    type(a)

Quand faut-il encadrer un tuple avec des parenthèses ? Par exemple si l'on crée une liste dont certains arguments sont des tuples.

.. ipython:: python

    [(1, 2), (3, 4)]
    [1, 2, 3, 4]
    [(1, 2), (3, 4)] == [1, 2, 3, 4]

Ou bien quand on on apelle une fonction dont un ou plusieurs arguments sont des tuples.

.. sourcecode:: ipython

    f((1, 2), (3, 4))   # fonction de deux arguments (deux tuples)
    f(1, 2, 3, 4)       # fonction de quatre arguments (quatre entiers)

Les opérateurs :code:`+` et :code:`+=` fonctionnent comme pour les listes.

.. ipython:: python

    (1,2) + (3,4)
    a = (1,2)
    a += (3,4)
    a


On peut **accéder** aux éléments d'un tuple de la même manière qu'on accède aux éléments d'une liste.

.. ipython:: python

    a = (1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e', 6, 'f')
    a[3]
    a[2:]
    a[:5]
    a[-3]
    a[2:9:2]
    a[8:1:-3]

Par contre, on ne peut pas **modifier** un tuple : on ne peut ni modifier ses éléments, ni en ajouter, ni en enlever.

.. sourcecode:: ipython

    s = (1, 2, 3)
    s[0] = 4

.. ipython:: python

    s = (1, 2, 3)
    s[0] = 4

A nouveau, la fonction :code:`len` renvoie la longueur d'un tuple.

.. ipython:: python

    len((1.23, 'abc', 45))



.. topic:: Affectations multiples


    Les tuples permettent d'affecter des valeurs à plusieurs variables en même temps [#affmul]_.

    .. ipython:: python

        a, b, c = 1, 2, 3
        a
        b
        c

    .. _affectations-multiples:

    Cela permet notamment d'échanger élégamment les valeurs de deux variables [#echange]_.

    .. ipython:: python

        a, b = 1, 2
        a
        b
        a, b = b, a
        a
        b


.. rubric:: Notes

.. [#tuple] Il s'agit exactement de la notion de *uplet* en mathématiques. L'appellation *tuple* provient en fait de l'anglais. En effet, en anglais, on parle de "quadruple", "quintuple", etc.. et plus généralement de :math:`n`-**tuple** tandis qu'en français, on emploie les termes "quadruplet", "quintuplet", etc.. et de manière générale :math:`n`-**uplet**. Néanmoins, la terminologie anglo-saxonne s'est imposée en ce qui concerne Python.

.. [#affmul] On peut également procéder à des affectations multiples à l'aide de listes.

    .. ipython:: python

        [a, b, c] = [1, 2, 3]
        a
        b
        c

.. [#echange] A nouveau, on peut également utiliser des listes pour échanger les valeurs de deux variables.

    .. ipython:: python

        [a, b] = [1, 2]
        a
        b
        [a, b] = [b, a]
        a
        b
