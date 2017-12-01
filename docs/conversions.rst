====================
Conversions de types
====================


On peut convertir un objet d'un type vers un autre type : il suffit pour cela d'utiliser le nom du type vers lequel on veut convertir. On parle alors de *conversion explicite*.

.. ipython:: python

    int('42')
    type(int('42'))

    str(25)
    type(str(25))

Il se peut que certaines conversions soient impossibles.

.. ipython:: python

    int('45f6')


L'utilisation d'opérateurs pour des objets dont le type n'est pas approprié peut donner lieu à des *conversions implicites*.

.. ipython:: python

    # Le booléen True est automatiquement converti en l'entier 1 pour pouvoir l'ajouter à l'entier 2
    True + 2

Mais il se peut qu'aucune conversion implicite ne puisse avoir lieu, ce qui conduit alors à une erreur.

.. ipython:: python

    'a' + 1.23
