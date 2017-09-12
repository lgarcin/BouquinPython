=======
Boucles
=======

Comme dans beau de langages de programmation, il existe deux types de boucles en Python :

    * les boucles inconditionnelles qui permettent d'exécuter un bloc d'instructions un nombre de fois fixé à l'avance ;

    * les boucles conditionnelles qui permettent l'exécution d'un code tant qu'une condition est remplie.


.. rubric:: Boucles inconditionnelles


Les boucles inconditionnelles en Python permettent de parcourir un objet de type **itérable** (comme une liste, un tuple ou une chaîne de caractères) élément par élément.

.. ipython:: python

    for elt in [1, 'toto', 2.34]:
        print(elt)
    for elt in 5, 6, 'tata':    # pas besoin de parenthèses pour le tuple dans ce cas
        print(elt)
    for elt in 'blabla':
        print(elt)


.. note::

    La fonction :code:`range` renvoie un itérable ... compteur blabla

    .. ipython:: python

        for i in range(5):
            print(i)
        for i in range(3, 8):
            print(i)
        for i in range(4, 9, 2):
            print(i)

.. todo:: blabla sur les itérables
.. todo:: listes par compréhension
