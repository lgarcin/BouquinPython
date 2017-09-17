=========
Fonctions
=========

Les fonctions en programmation ont deux objectifs :

    * réutilisation du code ;
    * abstraction : découpage d'une tâche complexe en tâches simples.


Considérons l'exemple simple



.. rubric:: Fonctions anonymes

En mathématiques, on peut parler d'une fonction de plusieurs manières.

    * On peut lui donner un nom : on peut par exemple considérer la fonction :math:`f` telle que :math:`f(x)=x^2`.
    * Mais si on ne compte pas réutiliser plus tard cette fonction, on peut tout simplement parler de la fonction :math:`x\mapsto x^2`.

De la même manière, on peut nommer explicitement une fonction.

::

    def f(x):
        return x**2

On peut également utiliser une fonction *anonyme* (ou encore fonction *lambda*).

::

    lambda x: x**2

.. ipython:: python

    (lambda x: x**2)(4)
    f = lambda x: x**2              # On peut bien sûr donner un nom à une fonction lambda
    f(4)
    g = lambda x, y: x**2 + y**2    # Une fonction lambda peut avoir plus d'un argument
    g(1, 2)


De manière générale, la syntaxe d'une fonction anonyme est la suivante.

::

    lambda <arguments>: <expression>

A la différence d'une fonction classique, une fonction anonyme ne nécessite pas de :code:`return` : l'expression suivant :code:`:` est renvoyée [#fctanonyme]_.



.. rubric:: Notes

.. [#fctanonyme] Une fonction anonyme peut également être employée pour accomplir une action plutôt que pour renvoyer une valeur.

.. ipython:: python

    f = lambda li: li.append('toto')
    a = [1, 2]
    f(a)
    a               # La fonction anonyme f a modifié la liste a
    print(f(a))     # Par contre, la fonction ne renvoie rien (en fait, renvoie None)


.. todo:: Syntaxe générale d'une fonction lambda, pas de multi-statements
.. todo:: Utilité des fonctions lambda
.. todo:: Parler de scope/portée

.. todo:: Documentation d'une fonction
.. todo:: parler des effets de bord ???
