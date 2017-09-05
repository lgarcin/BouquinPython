===============================
Tuples et chaînes de caractères
===============================

Tuples
------

Un *tuple* est tout à fait similaire à une liste : il s'agit d'une collection d'objets [#tuple]_ . On crée un tuple en séparant les objets par des des virgules :code:`,` et en les encadrant *éventuellement* par des parenthèses :code:`(...)`.

.. runblock:: pycon

    >>> type((1,2,3))
    >>> a = 1,2,3
    >>> type(a)

Quand faut-il encadrer un tuple avec des parenthèses ? Par exemple si l'on crée une liste dont certains arguments sont des tuples.

.. runblock:: pycon

    >>> [(1, 2), (3, 4)]
    >>> [1, 2, 3, 4]
    >>> [(1, 2), (3, 4)] == [1, 2, 3, 4]

Ou bien quand on on apelle une fonction dont un ou plusieurs arguments sont des tuples.

.. sourcecode:: ipython

    >>> f((1, 2), (3, 4))   # fonction de deux arguments (deux tuples)
    >>> f(1, 2, 3, 4)       # fonction de quatre arguments (quatre entiers)

Les opérateurs :code:`+` et :code:`+=` fonctionnent comme pour les listes.

.. runblock:: pycon

    >>> (1,2) + (3,4)
    >>> a = (1,2)
    >>> a += (3,4)
    >>> a


On peut **accéder** aux éléments d'un tuple de la même manière qu'on accède aux éléments d'une liste.

.. runblock:: pycon

    >>> a = (1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e', 6, 'f')
    >>> a[3]
    >>> a[2:]
    >>> a[:5]
    >>> a[-3]
    >>> a[2:9:2]
    >>> a[8:1:-3]

Par contre, on ne peut pas **modifier** un tuple : on ne peut ni modifier ses éléments, ni en ajouter [#modiftuple]_, ni en enlever.

.. sourcecode:: ipython

    >>> s = (1, 2, 3)
    >>> s[0] = 4

.. runblock:: pycon

    >>> s = (1, 2, 3)
    >>> s[0] = 4


.. topic:: Affectations multiples

    Les tuples permettent d'affecter des valeurs à plusieurs variables en même temps [#affmul]_.

    .. runblock:: pycon

        >>> a, b, c = 1, 2, 3
        >>> a
        >>> b
        >>> c

    Cela permet notamment d'échanger élégamment les valeurs de deux variables [#echange]_.

    .. runblock:: pycon

        >>> a, b = 1, 2
        >>> a
        >>> b
        >>> a, b = b, a
        >>> a
        >>> b

Chaînes de caractères
---------------------

Une chaîne de caractères n'est autre qu'une liste de caractères. Les caractères sont juxtaposés et encadrés par des guillemets simples :code:`'...'` ou doubles :code:`"..."`.

.. runblock:: pycon

    >>> "abcdef" == 'abcdef'

.. todo:: Imbriquer guillemets simples et doubles


A nouveau, les opérateurs :code:`+` et :code:`+=` fonctionnent comme pour les listes.

.. runblock:: pycon

    >>> 'abc' + "def"
    >>> s = 'abc'
    >>> s += "def"

On peut **accéder** de la même manière aux caractères d'une chaîne qu'aux éléments d'une liste.

.. runblock:: pycon

    >>> ma_chaine = "Bonjour Python"
    >>> ma_chaine[3]
    >>> ma_chaine[2:]
    >>> ma_chaine[:5]
    >>> ma_chaine[-3]
    >>> ma_chaine[2:9:2]
    >>> ma_chaine[8:1:-3]

Par contre, on ne peut pas non plus **modifier** une chaîne [#modifchaine]_.

.. sourcecode:: ipython

    >>> s = 'abc'
    >>> s[0] = 'z'

.. runblock:: pycon

    >>> s = 'abc'
    >>> s[0] = 'z'


Les chaînes possèdent de nombreuses méthodes : ces méthodes ne modifient jamais la chaîne de caractère mais renvoient une *autre* chaîne de caractère.

.. runblock:: pycon

    >>> ma_chaine = 'Mon nom est Bond. James Bond.'
    >>> ma_chaine.replace('Bond', 'Toto')
    >>> ma_chaine
    >>> ma_chaine.upper()
    >>> ma_chaine

.. todo:: mettre méthode dans glossaire



.. rubric:: Notes

.. [#tuple] Il s'agit exactement de la notion de *uplet* en mathématiques. L'appellation *tuple* provient en fait de l'anglais. En effet, en anglais, on parle de "quadruple", "quintuple", etc.. et plus généralement de :math:`n`-**tuple** tandis qu'en français, on emploie les termes "quadruplet", "quintuplet", etc.. et de manière générale :math:`n`-**uplet**. Néanmoins, la terminologie anglo-saxonne s'est imposée en ce qui concerne Python.

.. [#modiftuple] L'opérateur :code:`+=` ne modifie pas à proprement parler un tuple mais la valeur de la variable contenant initialement le tuple.

.. [#modifchaine] A nouveau, l'opérateur :code:`+=` modifie la valeur de la variable, pas la chaîne.

.. [#affmul] On peut également procéder à des affectations multiples à l'aide de listes.

    .. runblock:: pycon

        >>> [a, b, c] = [1, 2, 3]
        >>> a
        >>> b
        >>> c

.. [#echange] A nouveau, on peut également utiliser des listes pour échanger les valeurs de deux variables.

    .. runblock:: pycon

        >>> [a, b] = [1, 2]
        >>> a
        >>> b
        >>> [a, b] = [b, a]
        >>> a
        >>> b
