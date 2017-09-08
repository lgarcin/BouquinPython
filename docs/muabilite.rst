=========
Muabilité
=========

Il s'agit d'un paragraphe un peu subtil : il s'agit d'expliquer la différence fondamentale qu'il existe en Python entre les objets que l'on peut modifier (listes) ou que l'on ne peut modifier (tuples ou chaînes de caractère).


Considérons ce premier exemple où les variables sont des entiers.

.. runblock:: pycon

    >>> a = 1
    >>> b = a
    >>> a = 2           # on modifie a
    >>> a
    >>> b               # b n'a pas ete modifiee

Considérons maintenant l'exemple suivant où les variables sont des listes.

.. runblock:: pycon

    >>> a = [1, 2, 3]
    >>> b = a
    >>> a[0] = 'foo'    # on modifie la liste a
    >>> a
    >>> b               # la liste b a aussi ete modifiee !

Pour expliquer la différence entre ces deux exemples, il faut comprendre la représentation des objets Python en mémoire. Pour cela, on va utiliser la fonction :code:`id`. Pour schématiser, celle-ci renvoie l'emplacement en mémoire d'un objet.

.. runblock:: pycon

    >>> a = 1
    >>> b = a
    >>> id(a), id(b)    # les variables a et b pointent vers le meme emplacement en memoire
    >>> a = 2
    >>> id(a), id(b)    # la variable b pointe toujours vers le meme emplacement mais plus la variable b

L'instruction :code:`a = 2` a fait pointer la variable :code:`a` vers un autre emplacement en mémoire où est stocké l'entier :code:`2`.

.. tikz::
    :libs: positioning, arrows

    \node[rectangle,draw,pin={[draw,circle]120:b},pin={[draw,circle]240:a}](before){1};
    \node[rectangle,draw,pin={[draw,circle]60:b}](b after)[right=5cm of before]{1};
    \node[rectangle,draw,pin={[draw,circle]-60:a}](a after)[below=1cm of b after]{2};
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](before) -- (b after);

.. runblock:: pycon

    >>> a = [1, 2, 3]
    >>> b = a
    >>> id(a), id(b)    # les variables a et b pointent vers le meme emplacement en memoire
    >>> a[0] = 'foo'
    >>> id(a), id(b)    # les variables a et b pointent toujours vers le meme emplacement

Ici, l'instruction :code:`a[0] = 'foo'` a modifié l'objet stocké à l'emplacement commun vers lequel pointent les variables :code:`a` et :code:`b`. Comme :code:`a` et :code:`b` pointent toujours le même emplacement en mémoire, la variable :code:`b` est maintenant associée à ce nouvel objet.

.. tikz::
    :libs: positioning, arrows

    \node[rectangle,draw,pin={[draw,circle]120:b},pin={[draw,circle]240:a}](before){[1, 2, 3]};
    \node[rectangle,draw,pin={[draw,circle]60:b},pin={[draw,circle]-60:a}](after)[right=5cm of before]{['foo', 2, 3]};
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](before) -- (after);

Mais pourquoi cette différence de comportement ? Il existe en Python deux types d'objets : les objets **muables** et les objets **immuables**. On peut donner la définition suivante.

    Un objet est dit **muable** si on peut changer sa valeur après sa création. Il est dit **immuable** dans le cas contraire [#immuable]_.

Objets immuables
    Entiers, flottants, complexes, tuples, chaînes de caractères, ...

Objets muables
    Listes, dictionnaires, ...

Voilà la solution du mystère : toutes les variables pointant vers un même objet muable sont affectées par la modification de cet objet. Ceci ne peut pas se produire lorsque des variables pointent vers un objet immuable puisque celui-ci ne peut-être modifié.


.. note::

    Bien souvent, on veut copier une liste dans un nouvel objet pour qu'il ne subisse pas les modifications de l'objet initial. Pour cela, il ya plusieurs possibilités :

        * le slicing :code:`[:]` ;

        * l'utilisation de la méthode :code:`copy` ;

        * l'utilisation du constructeur :code:`list`.

    .. runblock:: pycon

        >>> liste1 = [1, 2, 3]
        >>> liste2 = liste1[:]
        >>> liste3 = liste1.copy()
        >>> liste4 = list(liste1)
        >>> id(liste1), id(liste2), id(liste3), id(liste4)  # les objets sont bien distincts
        >>> liste1[0] = 'toto'
        >>> liste1, liste2, liste3, liste4                  # liste1 a ete modifiee mais pas les autres listes

    .. todo:: constructeur dans glossaire


.. rubric:: Les opérateurs :code:`+` et :code:`+=`

Le lecteur attentif aura remarqué qu'on semblerait pouvoir modifier un objet immuable telle qu'une chaîne de caractères ou une liste à l'aide des opérateurs :code:`+` ou :code:`+=`. Mais ces opérateurs ne modifient pas l'objet en question ; ils créent en fait un **nouvel** objet. On peut s'en convaincre à l'aide de la fonction :code:`id`.

.. runblock:: pycon

    >>> t = (1, 2, 3)
    >>> id(t)
    >>> t = t + (4, 5)
    >>> t
    >>> id(t)

.. runblock:: pycon

    >>> t = (1, 2, 3)
    >>> id(t)
    >>> t += (4, 5)
    >>> t
    >>> id(t)

Pour les objets muables tels que les listes, les opérateurs :code:`+` et :code:`+=` se comportent de manières différentes : l'opérateur :code:`+` crée un nouvel objet tandis que l'opérateur :code:`+=` modifie l'objet initial.

.. runblock:: pycon

    >>> liste1 = [1, 2, 3]
    >>> liste2 = liste1
    >>> liste1 = liste1 + [4, 5]
    >>> liste1, liste2          # seule liste1 a ete modifiee
    >>> id(liste1), id(liste2)  # c'est normal : liste1 et liste2 pointent vers des objets distincts

.. runblock:: pycon

    >>> liste1 = [1, 2, 3]
    >>> liste2 = liste1
    >>> liste1 += [4, 5]
    >>> liste1, liste2          # liste1 et liste2 ont ete modifiees
    >>> id(liste1), id(liste2)  # c'est normal : liste1 et liste2 pointent vers le meme objet

.. rubric:: Egalité structurelle ou physique

On a vu que l'opérateur :code:`==` permettait de tester si deux objets étaient égaux. Mais de quel type d'égalité parle-t-on alors ? L'opérateur :code:`==` teste si deux objets ont la même **valeur** sans pour autant qu'il partage le même emplacement en mémoire. On parle alors d\\'**égalité structurelle**.

Lorsque "deux" objets sont en fait identiques (c'est-à-dire lorsqu'ils ont le même emplacement en mémoire), on parle d\\'**égalité physique**. Pour tester l'égalité physique, on peut comparer les emplacements en mémoire à l'aide de la fonction :code:`id` ou plus simplement utiliser l'opérateur :code:`is`.

.. runblock:: pycon

    >>> liste1 = [1, 2, 3]
    >>> liste2 = liste1
    >>> liste3 = liste1[:]
    >>> liste1, liste2, liste3
    >>> id(liste1), id(liste2), id(liste3)
    >>> liste2 == liste1, liste3 == liste1
    >>> liste2 is liste1, liste3 is liste1

Un exemple peut-être un peu plus surprenant.

.. runblock:: pycon

    >>> [1, 2, 3] == [1, 2, 3]
    >>> [1, 2, 3] is [1, 2, 3]

Python a en fait stocké deux versions de la liste :code:`[1, 2, 3]` dans deux emplacements en mémoire distincts.

-------

On termine par un cas plus vicieux que les deux exemples initiaux et qui peut faire passer des nuits blanches au programmeur débutant en Python.

.. runblock:: pycon

    >>> a = [[0] * 3] * 4
    >>> a
    >>> a[0][0] = 1     # on pense n'avoir modifie qu'un element de la liste de listes a
    >>> a               # en fait non...


.. rubric:: Notes

.. [#immuable] Ce n'est pas rigoureusement exact. Un objet immuable tel qu'un tuple peut contenir des objets muables comme des listes. Néanmoins, chaque objet du tuple conserve le même emplacement en mémoire même s'il a été modifié.

.. runblock:: pycon

    >>> a = ([1, 2, 3], 'toto', 'tata')
    >>> b = a
    >>> a[0][1] = 1000
    >>> a
    >>> b                   # b a egalement ete modifie
    >>> id(a[0]), id(b[0])  # le premier element du tuple est toujours le meme


.. todo:: immutabilité pour les fonctions
