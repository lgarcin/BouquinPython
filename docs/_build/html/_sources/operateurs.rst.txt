==========
Opérateurs
==========

Opérateurs arithmétiques
------------------------

Python dispose des opérateurs arithmétiques de base :code:`+` (addition), :code:`-` (soustraction), :code:`*` (multiplication) et :code:`/` (division).


.. runblock:: pycon

    >>> 1 + 2.3 * (4.5 - 6) / 7.8


L'exponentiation se fait à l'aide de l'opérateur :code:`**`.


.. runblock:: pycon

    >>> 8**3


Par ailleurs, les opérateurs :code:`%` et :code:`//` calculent respectivement le quotient et le reste d'une division euclidienne.


.. runblock:: pycon

    >>> 20%6
    >>> 20//6


Opérateurs de comparaison
-------------------------


Le résultat d'une comparaison est un booléen. Python dispose des opérateurs de comparaison :code:`<`, :code:`>`, :code:`<=`, :code:`>=`, :code:`==` (égalité), :code:`!=` (différence).

.. runblock:: pycon

    >>> 1 + 2 < 3.4
    >>> 5.6 >= 7
    >>> 1 + 1 == 2
    >>> "abc" != "def"


.. note::

    Il faut prendre garde de ne pas confondre l'opérateur d'**égalité** :code:`==` avec l'opérateur d'**affectation** :code:`=`.


Opérateurs logiques
-------------------


On dispose des opérateurs logique classiques : :code:`not` (négation), :code:`and` (conjonction) et :code:`or` (disjonction).

.. runblock:: pycon

    >>> not False
    >>> 1+2<3 and 4.5==6
    >>> 7<=8 or "abc"=="def"
