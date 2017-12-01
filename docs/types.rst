=====
Types
=====

.. todo:: Expliquer ce qu'est un type. En fait, on devrait parler de classe.

On décrit dans ce paragraphe les types de base utilisés par Python.

Booléen
-------

Un objet de type *booléen* peut prendre les valeurs logiques **vrai** (:code:`True`) ou **faux** (:code:`False`).


.. ipython:: python

    type(True)
    type(False)


Entier
------

Les entiers Python ne sont théoriquement pas limités en taille même si, en pratique, on est limité par la mémoire de la machine.


.. ipython:: python

    type(12)
    type(-34)

Flottant
--------

Les nombres non entiers (nombres "à virgule") sont stockés sous la forme de nombres *flottants*. La virgule est notée à l'anglo-saxonne à l'aide du caractère :code:`.`. On peut également utiliser la notation scientifique : :code:`1.23e45` signifie :math:`1,23\times10^{45}`.


.. ipython:: python

    type(1.23)
    type(1.)
    type(1.23e45)


Les nombres flottants sont en fait de la forme :math:`\pm m.2^e` où :math:`m` est un réel de l'intervalle :math:`[1,2[` appelé mantisse et :math:`e` est un entier. Les nombres :math:`m` et :math:`e` sont stockés sur un nombre fixé de bits [#ieee754]_ : il n'existe par conséquent qu'un nombre **fini** de nombres flottants.

Il faut bien comprendre que les nombres flottants ne sont en fait que des **approximations** des nombres réels que l'on considère, ce qui peut parfois créer des surprises.


.. ipython:: python

    2.3-1.5


Complexe
--------

Les nombres complexes se notent à l'aide de la lettre :code:`j` qui indique la partie imaginaire. Par exemple, le complexe :math:`1+2i` s'écrit :code:`1+2j`.


.. ipython:: python

    type(1.2+3.4j)

.. note::

    Pour représenter un complexe la lettre :code:`j` doit toujours être précédée d'un caractère numérique. Le complexe :math:`i` sera donc représenté par :code:`1j`.

On peut accéder aux parties réelle et imaginaire d'un nombre complexe grâce aux attributs :code:`real` et :code:`imag`.

.. ipython:: python

    z = 3 + 4j
    z.real
    z.imag

Dictionnaire (hors programme)
-----------------------------


.. ipython:: python

    type({'toto': 123, 'titi': 4.56, 'tata': 'abc'})


.. rubric:: Notes

.. [#ieee754] Pour plus de précision, on pourra consulter la définition de la norme `IEEE 754 <https://fr.wikipedia.org/wiki/IEEE_754>`_.


.. todo:: duck typing
