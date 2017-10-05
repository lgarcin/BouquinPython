============
Arithmétique
============

Décomposition d'un entier dans une base
=======================================

L'écriture d'un entier :math:`n\in\mathbb{N}^*` dans une base :math:`b` où :math:`b` est un entier supérieur ou égal à :math:`2` est une écriture de la forme

.. math::

    n=\sum_{k=0}^pa_kb^k

où les :math:`a_k` sont des entiers compris entre :math:`0` et :math:`b-1` et où :math:`a_p\neq0`. Par exemple, la décomposition en base :math:`8` de :math:`4621` est

.. math::

    1455= 7\times8^0+5\times8^1+6\times8^2+2\times8^3


On peut obtenir la liste :math:`[a_0,a_1,\dots,a_p]` à l'aide d'une suite de divisions euclidiennes par :math:`b`. Par exemple,

.. math::

    \begin{align*}
        1455 &= 7 + 8 \times 181\\
        181 &= 5 + 8 \times 22\\
        22 &= 6 + 8 \times 2
    \end{align*}

donc

.. math::

    4621 = 7 + 8 \times (5 + 8 \times (6 + 8 \times 2)) = 7 + 5 \times 8 + 6 \times 8^2 + 2 \times 8^4

.. ipython:: python

    def decomp(n, b):
        l = []
        while n != 0:
            l.append(n % b)
            n //= b
        return l

    decomp(24189, 10 )

    n, b = 3678, 7
    l = decomp(n, b)
    l
    sum([a * b ** i for i, a in enumerate(l)])  # On vérifie que la liste convient effectivement




Calcul de PGCD
==============

On peut implémenter l'algorithme d'Euclide en Python.

.. ipython:: python

    def pgcd(a, b):
        while b!= 0:
            a, b = b, a % b
        return abs(a)   # Le pgcd doit être positif

    pgcd(30, 12)
    pgcd(30, -12)

De même, on peut implémenter l'algorithme d'Euclide étendu qui, en plus du pgcd, donne des coefficients d'une relation de Bézout, c'est-à-dire des entiers :math:`u` et :math:`v` tels que

.. math::

    au+bv=\mathrm{pgcd}(a,b)

.. ipython:: python

    def bezout(a, b):
        s, t, u, v = 1, 0, 0, 1
        while b != 0:
            q = a // b
            a, s, t, b, u, v = b, u, v, a - q * b, s - q * u, t - q * v
        return (a, s, t) if a > 0 else (-a, -s, -t)     # Le pgcd doit être positif

    bezout(30, 12)
    bezout(30, -12)

.. todo:: se reporter au chapitre preuve pour comment ça marche.
.. todo:: peut-être un exemple quand même


Exponentiation rapide
=====================

Il s'agit ici de calculer efficacement une puissance entière d'un objet mathématique (nombre ou matrice par exemple). Un algorithme naïf serait le suivant.

.. ipython:: python

    def exponentiation(x, n):
        a = 1
        for _ in range(n):
            a *= x
        return a

    exponentiation(3, 5)

Il est clair que cet algorithme nécessite :math:`n` multiplications pour calculer une puissance :math:`n^\text{ème}`.

On peut proposer un léger raffinement pour éviter une multiplication.

.. ipython:: python

    def exponentiation2(x, n):
        if n == 0:
            return 1
        a = x
        for _ in range(n-1):
            a *= x
        return a

    exponentiation2(3, 5)


Mais on peut être beaucoup plus efficace. On remarque que toute puissance :math:`x^n` peut en fait s'écrire comme un produit de puissances de la forme :math:`x^{2^k}` : en effet, :math:`n` peut s'écrire comme une somme d'entiers de la forme :math:`2^k` en considérant sa décomposition en base :math:`2`.

.. math::

    x^{13}=x\times x^{12}=x\times(x^2)^6=x\times(x^4)^3=x\times x^4\times x^8

Il suffit alors de calculer successivement

.. ipython:: python

    def exponentiation_rapide(x, n):
        a = 1
        p = x
        while n > 0:
            if n % 2 == 1:
                a *= p
            p *= p
            n //= 2
        return a

    exponentiation_rapide(3, 5)

On peut également proposer un raffinement pour gagner une multiplication. En effet, à la dernière itération, l'instruction :code:`p *= p` est inutile puisque cette dernière valeur de :code:`p` ne sera pas utilisée. De plus, à la dernière itération, :code:`n` vaut :code:`1` qui est impair donc l'instruction :code:`a *= p` sera obligatoirement effectuée.

.. ipython:: python

    def exponentiation_rapide2(x, n):
        if n == 0:
            return 1
        a = 1
        p = x
        while n > 1:
            if n % 2 == 1:
                a *= p
            p *= p
            n //= 2
        return a * p

    exponentiation_rapide2(3, 5)

.. .. ipython:: python
..
..     %timeit exponentiation(3, 100)
..     %timeit exponentiation_rapide(3, 100)
..     %timeit 3**100
..     %timeit pow(3, 100)


Evaluation de polynômes
=======================

.. math::

    7 - 3X + 4X^2 + 5X^3 = 7 + X \left(-3 + 4X + 5X^2\right) = 7 + X \left(-3 + X \left(4 + 5X\right)\right)

.. ipython:: python

    def horner(poly, x):
        s = 0
        for c in poly:
            s = s * x + c
        return s

    horner([1, 2, 3], 4)
