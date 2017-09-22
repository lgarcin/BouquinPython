========================
Algorithmes de recherche
========================



Recherche d'un élément dans une liste
=====================================


Il faut noter que Python dispose déjà de l'opérateur :code:`in` pour tester si un élément figure dans une liste.

.. ipython:: python

    2 in [1, 2 ,3]
    4 in [1, 2, 3]

On peut néanmoins proposer notre propre algorithme : il suffit de balayer la liste et de renvoyer :code:`True` dès qu'on trouve l'élément recherché et :code:`False` si on a parcouru toute la liste sans trouver l'élément.

.. ipython:: python

    def appartient(elt, lst):
        for e in lst:
            if e == elt:
                return True
        return False

    appartient(2, [1, 2, 3])
    appartient(4, [1, 2, 3])


Recherche d'un élément dans une liste triée
===========================================

.. ipython:: python

    def appartient_dicho(elt, lst):
        g = 0
        d = len(lst) - 1
        while g <= d:
            m = (g + d) // 2
            if lst[m] == elt:
                return True
            if elt < lst[m]:
                d = m - 1
            else:
                g = m + 1
        return False

    appartient_dicho(2, [1, 2, 3])
    appartient_dicho(4, [1, 2, 3])

.. ipython:: python

    N = 100000
    from numpy.random import randint
    lst = [k for k in range(N)]
    %timeit appartient_dicho(randint(N), lst)

.. ipython:: python

    %timeit appartient(randint(N), lst)

.. ipython:: python

    from matplotlib.pyplot import plot
    @savefig recherche.png width=4in
    plot([1, 2, 3, 4], [4, 5, 6, 7])

.. plot::

    from matplotlib.pyplot import plot
    plot([4, 3, 2])
