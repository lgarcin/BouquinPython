=========
Variables
=========


Variable et affectation
-----------------------

Une *variable* est un objet qui associe un nom (*identifiant*) à une valeur stockée en mémoire. Concrètement, une variable permet de conserver une valeur en vue d'une utilisation ultérieure.

Pour stocker une valeur dans une variable, on utilise l'opérateur d'affectation :code:`=`.


.. runblock:: pycon

    >>> a = 2
    >>> b = 3
    >>> (a + b)**2


.. warning::

    Le symbole :code:`=` n'a pas du tout le même sens qu'en mathématiques. En mathématiques, ce symbole désigne un état de fait et a une valeur logique (une égalité peut être vraie ou fausse) tandis qu'en Python, il accomplit une action (stocker une valeur dans une variable).


Bien entendu, on peut changer la valeur d'une variable (d'où le nom) et même le type de cette valeur.


.. runblock:: pycon

    >>> a = 42
    >>> a
    >>> a = "toto"
    >>> a


Identifiant d'une variable
--------------------------

Bien que cela n'ait rien d'obligatoire, il est judicieux que l'identifiant d'une variable donne une indication quant à l'utilisation de cette variable. Par exemple, une variable devant contenir la
*moyenne* de plusieurs nombres sera plus judicieusement nommée :code:`moyenne` ou même :code:`moy` plutôt que :code:`x` ou :code:`toto`.

.. note::

    On ne peut pas choisir n'importe quel identifiant pour une variable.


    * Certains mots du langage Python sont dits "réservés" et ne peuvent servir à désigner une variable (:code:`for`, :code:`while`, :code:`del`, ...).

    * Le nommage des identifiants doit obéir à certaines règles : le premier caractère ne peut être un chiffre, certains caractères comme :code:`#` ou :code:`@` sont proscrits, ...


Opération/affectation
---------------------


Les opérateurs binaires peuvent être suivis du symbole :code:`=` pour effectuer simultanément une opération et une affectation. Ainsi :code:`a += b` équivaut à :code:`a = a + b`


.. runblock:: pycon

    >>> a = 2
    >>> a += 3
    >>> a
    >>> a *= 2
    >>> a
    >>> a **= 3
    >>> a
    >>> a %= 30
    >>> a
