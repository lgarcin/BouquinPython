=======
Boucles
=======

Comme dans beau de langages de programmation, il existe deux types de boucles en Python :

    * les boucles inconditionnelles qui permettent d'exécuter un bloc d'instructions un nombre de fois fixé à l'avance ;

    * les boucles conditionnelles qui permettent l'exécution d'un code tant qu'une condition est remplie.


Boucles inconditionnelles
=========================

Les boucles inconditionnelles en Python permettent de parcourir un objet de type **itérable** (comme une liste, un tuple ou une chaîne de caractères) élément par élément.

De manière générale, on utilise les mots-clés :code:`for` et :code:`in`.

::

    for <element> in <iterable>:
        <instruction1>
        <instruction2>
        ...

On peut itérer aussi bien sur des listes

.. ipython:: python

    for elt in [1, 'toto', 2.34]:
        print(elt)

que sur des tuples

.. ipython:: python

    for elt in 5, 6, 'tata':    # pas besoin de parenthèses pour le tuple dans ce cas
        print(elt)

et même sur des chaînes de caractère.

.. ipython:: python

    for elt in 'blabla':
        print(elt)


.. rubric:: La fonction :code:`range`

La fonction :code:`range` renvoie un itérable contenant des entiers. Plus précisément, lorsque :code:`a, b, c` sont des entiers (:code:`c!=0`),

    * :code:`range(a)` contient les entiers :code:`0, 1, 2, ..., a-2, a-1` (aucun si :code:`a <= 0`) ;

    .. ipython:: python

        for i in range(5):
            print(i)

    .. ipython:: python

        for i in range(-5):
            print(i)

    * :code:`range(a, b)` contient les entiers :code:`a, a+1, a+2, ..., b-2, b-1` (aucun si :code:`b <= a`) ;

    .. ipython:: python

        for i in range(3, 8):
            print(i)

    .. ipython:: python

        for i in range(8, 3):
            print(i)

    * :code:`range(a, b, c)` contient les entiers :code:`a, a+c, a+2c, ...` jusqu'à atteindre :code:`b` exclu (aucun si :code:`c*(b-a)<=0`).

    .. ipython:: python

        for i in range(4, 9, 2):
            print(i)

    .. ipython:: python

        for i in range(9, 4, 2):
            print(i)

    .. ipython:: python

        for i in range(9, 4, -2):
            print(i)

    .. ipython:: python

        for i in range(4, 9, -2):
            print(i)


Listes en compréhension
=======================

En mathématiques, il existe plusieurs manières de décrire un même ensemble. L'ensemble :math:`\mathcal{A}` des entiers pairs compris entre 0 et 19 peut être défini en *extension* :

.. math::

    \mathcal{A}=\{0,2,4,6,8,10,12,14,16,18\}

Il peut également être décrit en *compréhension* :

.. math::

    \mathcal{A}=\{2n,\;n\in[\![0,9]\!]\}

De la même manière, la liste de ces entiers peut être défini en Python en extension :

.. ipython:: python

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

et en compréhension :

.. ipython:: python

    [2*n for n in range(10)]

On parle alors de *liste en compréhension*.

Une autre manière de définir :math:`\mathcal{A}` en compréhension est la suivante :

.. math::

    \mathcal{A} = \{x\in[\![0,19]\!],\;x\equiv0[2]\}

La version correspondante en Python est :

.. ipython:: python

    [n for n in range(20) if n%2==0]

Bien entendu, on peut utiliser ce type de liste pour d'autres objets que des entiers [#listcomp]_.

.. ipython:: python

    [s.upper() for s in ('toto', 'tata', 'titi', 'zozo', 'zaza', 'zizi') if s[0]=='t']



Boucles conditionnelles
=======================

Une boucle conditionnelle consiste à répéter un bloc d'instructions **tant qu'une condition est vraie**.


.. rubric:: Notes

.. [#listcomp] Les listes en compréhension peuvent être utilisées pour effectuer des actions plutôt que de calculer des valeurs.

    .. ipython:: python

        s = ([], [1, 2], ['titi', 'tata'])
        [li.append('toto') for li in s]
        s


.. todo:: blabla sur les itérables
.. todo:: break et continue
