==========
Mutabilité
==========

Il s'agit d'un paragraphe un peu subtil : on expliquera notamment pourquoi il existe en Python des objets **modifiables** (comme les listes) et des objets **non modifiables** (comme les tuples ou les chaines). On parlera plutôt d'objets **mutables** ou **immutables** (c'est à nouveau un anglicisme).


Considérons ce premier exemple où les variables sont des entiers.

.. runblock:: pycon

    >>> a = 1
    >>> b = a
    >>> a = 2           # on modifie a
    >>> a
    >>> b               # b n'a pas ete modifiee

Considérons maintenant l'exemple suivant où les variables sont des listes.

.. runblock:: pycon

    >>> a = [1, 2]
    >>> b = a
    >>> a[0] = 'foo'    # on modifie la liste a
    >>> a
    >>> b               # la liste b a aussi ete modifiee !

Pour expliquer la différence entre ces deux exemples, il faut comprendre la représentation des objets Python en mémoire. Pour cela, on va utiliser la fonction :code:`id`. Pour schématiser, celle-ci renvoie l'emplacement en mémoire de l'objet lié à une variable.

.. runblock:: pycon

    >>> a = 1
    >>> b = a
    >>> id(a), id(b)    # les variables a et b pointent vers le meme emplacement en memoire
    >>> a = 2
    >>> id(a), id(b)    # la variable b pointe toujours vers le meme emplacement mais plus la variable b

L'instruction :code:`a=2` a donc utilisé un nouvel emplacement en mémoire pour stocker l'entier 2 et fait pointer la variable :code:`a` vers ce nouvel emplacement.

.. runblock:: pycon

    >>> a = [1, 2]
    >>> b = a
    >>> id(a), id(b)    # les variables a et b pointent vers le meme emplacement en memoire
    >>> a[0] = 'foo'
    >>> id(a), id(b)    # les variables a et b pointent toujours vers le meme emplacement

Ici, l'instruction :code:`a[0]='foo'` a modifié l'objet stocké à l'emplacement commun vers lequel pointent les variables :code:`a` et :code:`b`. Comme :code:`a` et :code:`b` pointent toujours le même emplacement en mémoire, la variable :code:`b` est maintenant associée à ce nouvel objet.

Les choses s'éclaireront sans doute plus à l'aide d'un schéma.

.. tikz:: An Example Directive with Caption
    :libs: positioning, arrows

    \node[rectangle,draw,pin={[draw,circle]120:b},pin={[draw,circle]240:a}](before){123};
    \node[rectangle,draw,pin={[draw,circle]60:b}](b after)[right=5cm of before]{123};
    \node[rectangle,draw,pin={[draw,circle]-60:a}](a after)[below=1cm of b after]{456};
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](before) -- (b after);


.. tikz:: An Example Directive with Caption
    :libs: positioning, arrows

    \node[rectangle,draw,pin={[draw,circle]120:b},pin={[draw,circle]240:a}](before){[1,2,3]};
    \node[rectangle,draw,pin={[draw,circle]60:b},pin={[draw,circle]-60:a}](after)[right=5cm of before]{[4,5,6]};
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](before) -- (after);


Définition (bof)

    Un objet est dit **mutable** si on peut changer sa valeur sans changer son emplacemenent en mémoire. Dans le cas contraire, l'objet est dit **immutable**.


On peut tomber sur des problèmes nettement plus vicieux qui peuvent se

.. runblock:: pycon

    >>> a = [[0] * 3] * 4
    >>> a
    >>> a[0][0] = 1     # on pense n'avoir modifie qu'un element de la liste de listes a
    >>> a               # en fait non...





.. todo:: immutabilité pour les fonctions

.. todo:: comment copier une liste -> slicing

.. todo:: égalité structurelle/égalité physique ==/is
