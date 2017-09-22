======
Listes
======

Création de listes et opérations de base
========================================

Une **liste** est tout simplement une collection d'objets. On la déclare en séparant ses éléments par des virgules :code:`,` et en les encadrant par des crochets :code:`[...]`.


.. ipython:: python

    type([1,2,3])


Les objets contenus dans une même liste peuvent être de types différents.


.. ipython:: python

    [1.23, 'abc', 45]


On peut même imbriquer des listes.


.. ipython:: python

    [1.23, ["abc", "def", "ghi"], [45, 67]]


L'opérateur :code:`+` permet de *concaténer* des listes.


.. ipython:: python

    [1.23, 'abc', 45] + [6, 'def', 'ghi', 7.89]


On devine alors l'action de l'opérateur :code:`*` [#monoide]_.


.. ipython:: python

    [1.23, 'abc', 45] * 3


.. note::

    On ne peut évidemment multiplier une liste que par un **entier**.


La fonction :code:`len` permet de récupérer la longueur d'une liste.


.. ipython:: python

    len([1.23, 'abc', 45])


Accès aux éléments
==================

On peut accéder aux éléments d'une liste via leurs indices et l'opérateur :code:`[ ]`.


.. ipython:: python

    ma_liste = [25, 34, 48, 67]
    ma_liste[2]

.. warning::

  Il est à noter que les indices des listes commencent à 0 et non 1. Le dernier indice d'une liste de :math:`n` éléments est donc :math:`n-1` et non :math:`n`.

On peut bien sûr accéder à des éléments de listes imbriquées.


.. ipython:: python

    ma_liste = [1.23, ["abc", "def", "ghi"], [45, 67]]
    ma_liste[1][2]


On peut également accéder à des éléments d'une liste "par la fin".


.. ipython:: python

    ma_liste = ['a', 'b', 'c', 'd', 'e']
    ma_liste[-1]
    ma_liste[-3]


Modification des éléments
=========================

L'opérateur :code:`[ ]` permet également de modifier les éléments d'une liste.


.. ipython:: python

    ma_liste = [25, 34, 48, 67]
    ma_liste[2] = 666
    ma_liste


Bien évidemment, cela fonctionne aussi pour les listes imbriquées.

.. ipython:: python

    ma_liste = [1.23, ["abc", "def", "ghi"], [45, 67]]
    ma_liste[1][2] = "toto"
    ma_liste


Insertion et suppression d'éléments
===================================

Il existe plusieurs moyens d'ajouter des éléments à une liste.

La première méthode est de les ajouter un par un grâce aux méthodes :code:`append` (insertion en fin de liste) ou :code:`insert` (insertion à un endroit donné).


.. ipython:: python

    ma_liste = ['a', 1, 'b']
    ma_liste.append(2)
    ma_liste
    ma_liste.insert(2, 'toto')
    ma_liste


Pour ajouter plusieurs éléments d'affilée, on peut utiliser l'opérateur de concaténation :code:`+` ou de concaténation/affectation :code:`+=` ou encore la méthode :code:`append`.

.. todo:: mettre méthode dans glossaire

.. ipython:: python

    ma_liste = ['a', 1, 'b', 2]
    ma_liste = ma_liste + ['c', 3, 'd']
    ma_liste
    ma_liste += [4, 5]
    ma_liste
    ma_liste.extend(['e', 6, 'f'])
    ma_liste

De même, il existe plusieurs façons de supprimer des éléments d'une liste.

Pour supprimer des éléments, on peut utiliser les méthodes :code:`pop` (renvoie le dernier élément et le supprime de la liste) ou :code:`remove` (supprime un élément de valeur donnée).

.. todo:: mettre méthode dans glossaire


.. ipython:: python

    ma_liste = ['a', 1, 'b', 2, 'c', 3]
    ma_liste.pop()
    ma_liste
    ma_liste.remove('b')
    ma_liste


.. note::

    La méthode :code:`remove` ne supprime que la *première* occurence d'une valeur donnée.


    .. ipython:: python

        ma_liste = [1, 2, 3, 2, 4, 2]
        ma_liste.remove(2)
        ma_liste


La suppression d'éléments peut également se faire au moyen du mot-clé :code:`del` [#del]_.


.. ipython:: python

    ma_liste = ['a', 1, 'b', 2, 'c', 3]
    del ma_liste[2]
    ma_liste


Sous-listes (slicing)
=====================

Il existe une syntaxe permettant de créer une sous-liste d'une liste.


.. ipython:: python

    ma_liste = ['a', 'b', 'c', 'd', 'e', 'f']
    ma_liste[2:5]


De manière générale, si :code:`li` est une liste, alors :code:`li[a:b]` renvoie la liste formée des éléments de la liste :code:`li` dont les indices sont compris entre :code:`a` (**inclus**) et :code:`b` (**non inclus**).

Si :code:`a` ou :code:`b` sont omis, la sélection s'opére à partir du début ou jusqu'à la fin de la liste.


.. ipython:: python

    ma_liste = ['a', 'b', 'c', 'd', 'e', 'f']
    ma_liste[2:]
    ma_liste[:4]


On peut encore sélectionner des éléments à intervalles réguliers.


.. ipython:: python

    ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    ma_liste[2:9:3]
    ma_liste[7:2:-2]


Le slicing permet aussi de modifier les éléments d'une liste.

.. ipython:: python

    ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    ma_liste[2:9:3]
    ma_liste[2:9:3] = 'toto', 'tata', 'titi'
    ma_liste


On peut combiner le slicing et le mot-clé :code:`del` pour supprimer plusieurs éléments à la fois.


.. ipython:: python

    ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    ma_liste[5:10:2]
    del ma_liste[5:10:2]
    ma_liste



.. rubric:: Notes

.. [#monoide] En termes savants, l'ensemble des listes munis de la loi :code:`+` est un *monoïde*. La loi :code:`+` est en effet une loi interne associative et la liste vide :code:`[]` est neutre pour cette loi. Le "produit" d'une liste par un entier (positif) n'est autre qu'un *multiple* de cette liste.

.. [#del] De manière générale, le mot-clé :code:`del` "supprime" une variable (sans rentrer dans les détails).

    .. ipython:: python

        a = 42
        del a
        a
