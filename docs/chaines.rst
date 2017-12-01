====================
Chaînes de caractère
====================

Une chaîne de caractères n'est autre qu'une liste de caractères. Les caractères sont juxtaposés et encadrés par des guillemets simples :code:`'...'` ou doubles :code:`"..."`.

.. ipython:: python

    type('abcdef')
    "abcdef" == 'abcdef'

.. todo:: Imbriquer guillemets simples et doubles

A nouveau, les opérateurs :code:`+` et :code:`+=` fonctionnent comme pour les listes.

.. ipython:: python

    'abc' + "def"
    s = 'abc'
    s += "def"

On peut **accéder** de la même manière aux caractères d'une chaîne qu'aux éléments d'une liste.

.. ipython:: python

    ma_chaine = "Bonjour Python"
    ma_chaine[3]
    ma_chaine[2:]
    ma_chaine[:5]
    ma_chaine[-3]
    ma_chaine[2:9:2]
    ma_chaine[8:1:-3]

Par contre, on ne peut pas **modifier** une chaîne.

.. ipython:: python

    s = 'abc'
    s[0] = 'z'

Encore une fois, la fonction :code:`len` renvoie la longueur d'une chaîne de caractères.

.. ipython:: python

    len('Anticonstitutionnellement')

Les chaînes possèdent de nombreuses méthodes : ces méthodes ne modifient jamais la chaîne de caractère mais renvoient une *autre* chaîne de caractère.

.. ipython:: python

    ma_chaine = 'Mon nom est Bond. James Bond.'
    ma_chaine.replace('Bond', 'Toto')
    ma_chaine
    ma_chaine.upper()
    ma_chaine

.. todo:: mettre méthode dans glossaire
