=========
Variables
=========


Variable et affectation
-----------------------

Une *variable* est un objet qui associe un nom (*identifiant*) à un objet stocké en mémoire. Concrètement, une variable permet de conserver un objet en vue d'une utilisation ultérieure.

Pour stocker un objet dans une variable, on utilise l'opérateur d'affectation :code:`=`.


.. ipython:: python

    a = 2
    b = 3
    (a + b)**2


.. warning::

    Le symbole :code:`=` n'a pas du tout le même sens qu'en mathématiques. En mathématiques, ce symbole désigne un état de fait et a une valeur logique (une égalité peut être vraie ou fausse) tandis qu'en Python, il accomplit une action (stocker une valeur dans une variable).

Bien entendu, on peut changer la valeur d'une variable (d'où le nom) et même le type de cette valeur.


.. ipython:: python

    a = 42
    a
    a = "toto"
    a


.. topic:: Echange de deux variables

    On est souvent amené à échanger les valeurs de deux variables. La méthode naïve ne fonctionne pas.

    .. ipython:: python

        a = 1
        b = 2
        a = b # Les deux variables valent 2 !
        b = a
        a
        b

    L'idée est alors d'employer une variable auxiliaire.

    .. ipython:: python

        a = 1
        b = 2
        aux = a
        a = b
        b = aux
        a
        b

    On peut également utiliser des :ref:`affectations multiples <affectations-multiples>` à l'aide de tuples ou de listes.


Identifiant d'une variable
--------------------------

Bien que cela n'ait rien d'obligatoire, il est judicieux que l'identifiant d'une variable donne une indication quant à l'utilisation de cette variable. Par exemple, une variable devant contenir la
*moyenne* de plusieurs nombres sera plus judicieusement nommée :code:`moyenne` ou même :code:`moy` plutôt que :code:`x` ou :code:`toto`.

.. note::

    On ne peut pas choisir n'importe quel identifiant pour une variable.


    * Certains mots du langage Python sont dits "réservés" et ne peuvent servir à désigner une variable (:code:`for`, :code:`while`, :code:`del`, ...).

    * Le nommage des identifiants doit obéir à certaines règles : le premier caractère ne peut être un chiffre, certains caractères comme :code:`#` ou :code:`@` sont proscrits, ...
