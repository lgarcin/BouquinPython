============
Probabilités
============

Statistiques
============

Le calcul de la moyenne est on ne peut plus simple : il s'agit de la somme des éléments de la liste divisée par le nombre d'éléments de cette liste [#numpy_moyenne]_. De manière plus formmelle, la moyenne :math:`m` d'une liste :math:`(x_1,\dots,x_n)` de nombres est

.. math::

    m=\frac{1}{n}\sum_{k=1}^nx_k

.. ipython:: python

    def moyenne(liste):
        somme = 0
        for el in liste:
            somme += el
        return somme / len(liste)

    moyenne([1, 2, 3])


On peut donner deux expressions de la variance :math:`v` d'une liste :math:`(x_1,\dots,x_n)` de nombres dont on dispose déjà de la moyenne :math:`m`.

.. math::

    v = \left(\frac{1}{n}\sum_{k=1}^nx_k^2\right)-m^2 = \frac{1}{n}\sum_{k=1}^n(x_k-m)^2


En utilisant la première expression, on peut par exemple donner cette fonction de calcul de la variance [#numpy_variance]_.

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


Simuler une variable aléatoire
==============================

Dans la suite, on fera appel à la fonction :code:`random` du module :code:`random` qui renvoie un flottant tiré aléatoirement dans l'intervalle :math:`[0,1[`.

.. ipython:: python

    from random import random

    [random() for _ in range(10)]

Cela nous permettra de simuler des variables aléatoires connaissant leurs lois [#numpy_random]_.

On cherche dans un premier temps à simuler une variable aléatoire :math:`X` **à valeurs dans un ensemble fini**, disons :math:`\{0,\dots,n-1\}` où :math:`n\in\mathbb{N}^*`, dont on connaît la loi, c'est-à-dire les valeurs de :math:`\mathbb{P}(X=k)` pour :math:`k\in\{0,\dots,n-1\}`.

On construit pour cela une fonction prenant pour argument la loi d'une telle variable aléatoire sous la forme d'une liste de réels positifs de somme 1.

.. ipython:: python

    def simul(loi):
        proba = random()
        s = 0
        for i, p in enumerate(loi):
            s += p
            if proba < s:
                return i

.. ipython:: python

    [simul([.3, .5, .2]) for _ in range(20)]

On désire maintenant simuler une variable aléatoire :math:`X` **à valeurs dans un ensemble dénombrable**, disons :math:`\mathbb{N}`, dont on connaît la loi, c'est-à-dire les valeurs de :math:`\mathbb{P}(X=k)` pour :math:`k\in\mathbb{N}`.

La loi de cette variable aléatoire ne peut alors plus être représentée sous la forme d'une liste finie ; on la représente donc comme une fonction d'argument un entier :math:`n` et renvoyant :math:`\mathbb{P}(X=n)`.

.. ipython:: python

    def simul(loi):
        proba = random()
        s = loi(0)
        n = 0
        while proba >= s:
            n += 1
            s += loi(n)
        return n

.. ipython:: python

    from math import factorial, exp

    # Simulation d'une loi de Poisson
    poisson = lambda l: lambda n: exp(-l) * l**n / factorial(n)
    [simul(poisson(2)) for _ in range(20)]


Pour terminer, on peut facilement simuler une variable suivant une **loi binomiale** puisque l'on sait qu'elle est de même loi qu'une somme de variables de Bernoulli indépendantes.

.. ipython:: python

    def bernoulli(p):
        return 1 if random() < p else 0

    def binomiale(n, p):
        return sum(bernoulli(p) for _ in range(n))

    [binomiale(5, .8) for _ in range(20)]

    [binomiale(5, .2) for _ in range(20)]


.. [#numpy_moyenne] Evidemment, Python dispose déjà deux fonctions permettant de calculer aisément la moyenne d'une liste de nombres. On peut par exemple utiliser la fonction :code:`sum` qui, comme son nom l'indique, calcule la somme des éléments d'une liste (ou plus généralement d'un objet de type itérable).

    .. ipython:: python

        moyenne = lambda liste: sum(liste) / len(liste)

        moyenne([1, 2, 3])

    Le module :code:`numpy` dispose même d'une fonction :code:`mean` (*moyenne* en anglais).

    .. ipython:: python

        from numpy import mean

        mean([1, 2, 3])

.. [#numpy_variance] Bien entendu, le module :code:`numpy` dipose déjà d'une fonction ad hoc : la fonction :code:`var`.

    .. ipython:: python

        from numpy import var

        var([1, 2, 3])

.. [#numpy_random] A nouveau, le module :code:`numpy.random` dispose déjà de fonctions permettant de simuler la plupart des lois classiques.
