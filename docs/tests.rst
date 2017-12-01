=====
Tests
=====

Un test permet d'effectuer un bloc d'instructions lorsqu'une condition est remplie. On emploie pour cela le mot-clé :code:`if` suivie d'une expression à valeur booléenne.

.. ipython:: python

    a = 4       # Changer la valeur de a pour comprendre ce qui se passe
    if a % 2 ==0 :
        print('a est pair')


Si on veut introduire un bloc d'instructions à exécuter lorsque la condition **n'est pas** remplie, on emploie le mot-clé :code:`else`.

.. ipython:: python

    a = 5
    if a % 2 == 0:
    ...  print('a est pair')
    else:
    ...  print('a est impair')


Si on veut envisager plusieurs tests successifs, on emploie le mot-clé :code:`elif` (conctraction de :code:`else if`).

.. ipython:: python

    a = 5
    if a % 2 == 0:
    ...  print('a est pair')
    elif a > 3:
    ...  print('a est impair et strictement supérieur à 3')

On peut évidemment combiner :code:`if`, :code:`elif` et :code:`else`.

.. ipython:: python

    a = 1
    if a % 2 == 0:
    ...  print('a est pair')
    elif a > 3:
    ...  print('a est impair et strictement supérieur à 3')
    else:
    ...  print('a est impair et inférieur ou égal à 3')

Opérateur ternaire :code:`... if ... else ...`
==============================================

Python dispose

::

    <expression1> if <condition> else <expression2>

Cette expression est évaluée comme :code:`<expression1>` si :code:`<condition>` est vraie et comme :code:`<expression2>` sinon.

.. ipython:: python

    a = 0
    'papa' if a == 0 else 'maman'
    'papa' if a == 1 else 'maman'

Ce type d'expression peut également accomplir une action plutôt que de renvoyer un objet.

.. ipython:: python

    li = [1, 2, 3]
    a = 0
    li.append('toto') if a == 0 else li.append('titi')
    li
    # En fait, l'expression est évaluée à None
    print(li.append('toto') if a == 1 else li.append('titi'))
    li
