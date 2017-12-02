=========
Fonctions
=========

Une fonction est un bloc d'instructions que l'on peut appeler à tout moment d'un programme.


Au cours des chapitres précédents, on a déjà rencontré de nombreuses fonctions telles que :code:`print` ou :code:`len`. De manière générale, une fonction est une "boîte noire" à laquelle on fournit une ou plusieurs valeurs et qui calcule une nouvelle valeur ou effectue des actions à partir de ces données.

Définir une fonction
====================

Considérons l'exemple simple suivant.

.. todo:: A terminer

Il faut bien faire la différence entre **la déclaration** et **l'appel** de la fonction. Lorsqu'une fonction est **déclarée**, aucun code n'est exécuté. Il faut **appeler** la fonction pour que le code soit exécuté.

Les fonctions en programmation ont essentiellement deux objectifs :

    * réutilisation du code ;
    * découpage d'une tâche complexe en tâches simples.



::

    def <nom_fonction>(<arguments>):    # En-tête de la fonction
        <instruction1>
        <instruction2>                  # Corps de la fonction
        ...
        return <valeur>

.. todo:: rien ne se passe après avoir atteint un return

.. note:: Une fonction peut n'avoir aucun argument.

    .. ipython:: python

        def f():
            return 1

        f()


.. todo:: le nom des arguments n'importe pas comme en maths
.. todo:: on peut déclarer une fonction dans une autre fonction.
.. todo:: arguments facultatifs et arguments par défaut
.. todo:: la déclaration d'une fonction ne fait rien



Fonction vs. procédure
======================

Une fonction peut ne pas contenir d'instruction :code:`return` ou peut ne renvoyer aucune valeur. Dans ce cas, on parlera de *procédure* plutôt que de fonction. En fait, si on ne renvoie pas explicitement de valeur, Python renverra par défaut la valeur particulière :code:`None`.

.. ipython:: python

    def f(x):
        x**2

.. ipython:: python

    print(f(2))

.. ipython:: python

    def g(x):
        2 * x
        return

.. ipython:: python

    print(g(2))

.. warning::

    Une erreur de débutant consiste à confondre les utilisations de :code:`print` et :code:`return` : une fonction ne compotant qu'un :code:`print` et pas de :code:`return` ne fera qu'afficher un résultat à l'écran mais ne renverra aucune valeur.

    .. ipython:: python

        def bidon():
            print(1)
            return 2

        a = bidon() # La fonction bidon affiche bien 1
        a           # Mais elle a renvoyé la valeur 2

La plupart du temps, on préfèrera utiliser utiliser :code:`return` plutôt que :code:`print` : l'objet affiché par :code:`print` est en quelque sorte "perdu" pour le reste du programme s'il n'a pas été renvoyé via :code:`return`.

.. ipython:: python

    def liste_carres1(n):
        print([k**2 for k in range(1, n+1)])

.. ipython:: python

    def liste_carres2(n):
        return [k**2 for k in range(1, n+1)]

.. ipython:: python

    # Avec la première version, la liste des carrés est affichée mais on ne peut plus rien en faire
    liste_carres1(10)
    # En effet, la fonction renvoie None
    print(liste_carres1(10))
    # Avec la deuxième version, on peut par exemple calculer la somme des carrés des premiers entiers
    sum(liste_carres2(10))

Portée des variables
====================

Une fonction peut utiliser des variables définies **à l'extérieur** de cette fonction.

.. ipython:: python

    a = 2
    def f(x):
        return a * x

    f(5)

On dit que les variables définies à l'extérieur d'une fonction sont des variables **globales**.

.. note::

    De manière générale, il est plutôt déconseillé d'utiliser des variables globales à l'intérieur d'une fonction. De toute façon, il est toujours possible de passer une variable globale en tant qu'argument d'une fonction.

.. warning::

    Si on veut utiliser une variable globale à l'intérieur d'une fonction, il faut que celle-ci soit déclarée **avant** l'appel de cette fonction.

    .. ipython:: python

        def f(x):
            return b * x

        f(5)
        b = 2

Considérons maintenant l'exemple suivant.

.. ipython:: python

    a = 1
    def f():
        a = 2

.. ipython:: python

    a
    f()
    a   # a vaut toujours 1


On dit que les variables à l'intérieur d'une fonction sont des variables **locales**. Cela signifie en particulier que des opérations effectuées sur une variable d'un certain nom **à l'intérieur** d'une fonction ne modifient pas une variable du même nom **à l'extérieur** de cette fonction.

.. note::

    On évitera cependant de donner des noms identiques à des variables locales et globales de manière à éviter toute confusion.

Quand il existe des variables locales et globales de même nom, la préférence est donnée aux variables locales à l'intérieur de la fonction.

.. ipython:: python

    a = 1
    def f(x):
        a = 3
        return a + x    # la variable locale a est utilisée et non la variable globale a

.. ipython:: python

    f(5)



On ne peut pas accéder à des variables locales à l'extérieur de la fonction où elles sont définies.

.. ipython:: python

    def f():
        c = 2

.. ipython:: python

    c   # c est inconnu à l'extérieur de la fonction

On peut donc également voir les variables locales comme des variables *temporaires* dont l'existence n'est assurée qu'à l'intérieur de la fonction où elles interviennent.

On peut néanmoins modifier une variable globale à l'intérieur d'une fonction : on utilise alors le mot-clé :code:`global`.

.. ipython:: python

    a = 1
    def f():
        global a
        a = 2

.. ipython:: python

    a
    f()
    a   # a vaut bien 2


Les arguments d'une fonction ont également une portée locale.

.. ipython:: python

    def f(x):
        return 2 * x

    x   # x est inconnu à l'extérieur de la fonction


Fonctions et mutabilité
=======================

Considérons ce premier exemple où l'argument et un entier.

.. ipython:: python

    def f(x):
        x += 1

.. ipython:: python

    a = 2
    f(a)
    a           # la variable a n'est pas modifiée

Et maintenant, un deuxième exemple où l'argument est une liste.

.. ipython:: python

    def g(li):
        li.append(3)

.. ipython:: python

    lst = [1, 2]
    g(lst)
    lst       # la variable lst a été modifiée

Le résultat du deuxième exemple peut sembler étrange puisqu'une variable globale a été modifiée à l'intérieur d'une fonction. Pour expliquer cette différence de comportement, il faut comprendre plus en détail comment sont passés les arguments à une fonction et faire une distinction entre les objets *mutables* et *immutables*.

* Lors de l'exécution des instructions :code:`f(a)` et :code:`g(lst)`, les emplacements en mémoire dans lesquels sont stockés les objets associés aux variables :code:`a` et :code:`lst` (c'est-à-dire l'entier :code:`2` et la lst :code:`[1, 2]`) sont passés aux fonctions :code:`f` et :code:`g` et les paramètres :code:`x` et :code:`li` pointent alors vers ces emplacements en mémoire.
* Puisqu'un entier est un objet immutable, l'instruction :code:`x += 1` fait pointer le paramètre :code:`x` vers un nouvel emplacement mémoire où est stocké l'entier :code:`3`. Cependant, a variable :code:`a` pointe toujours vers l'ancien emplacement en mémoire et est donc toujours associée à l'entier :code:`2`.

.. tikz::
    :libs: positioning, arrows

    \node[rectangle,draw,pin={[draw,circle]120:a}](init){2};
    \node[rectangle,draw,pin={[draw,circle]90:a},pin={[draw,circle]-90:x}](beginfunc)[right=3cm of init]{2};
    \node[rectangle,draw,pin={[draw,circle]90:a}](a endfunc)[right=3cm of beginfunc]{2};
    \node[rectangle,draw,pin={[draw,circle]-90:x}](x endfunc)[below=1cm of a endfunc]{3};
    \node[rectangle,draw,pin={[draw,circle]60:a}](final)[right=3cm of a endfunc]{2};
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](init) --node[midway,above]{Appel f(a)} (beginfunc);
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](beginfunc) --node[midway,above]{x += 1} (a endfunc);
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](a endfunc) --node[midway,above]{Sortie de f} (final);

* Par contre, une liste étant un objet mutable, l'instruction :code:`li.append(3)` modifie l'objet stocké à l'emplacement en mémoire vers lequel pointe :code:`li`. Cet objet vaut alors :code:`[1, 2, 3]`. Mais la variable :code:`lst` pointe toujours vers le même emplacement en mémoire et est donc associé à cet objet modifié.

.. tikz::
    :libs: positioning, arrows

    \node[rectangle,draw,pin={[draw,circle]120:lst}](init){[1, 2]};
    \node[rectangle,draw,pin={[draw,circle]90:lst},pin={[draw,circle]-90:li}](beginfunc)[right=3cm of init]{[1, 2]};
    \node[rectangle,draw,pin={[draw,circle]90:lst},pin={[draw,circle]-90:li}](endfunc)[right=3cm of beginfunc]{[1, 2, 3]};
    \node[rectangle,draw,pin={[draw,circle]60:lst}](final)[right=3cm of endfunc]{[1, 2, 3]};
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](init) --node[midway,above]{Appel g(lst)} (beginfunc);
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](beginfunc) --node[midway,above]{li.append(3)} (endfunc);
    \draw[-fast cap,shorten <=10pt,shorten >=10pt,>=latex, blue!20!white, line width=10pt](endfunc) --node[midway,above]{Sortie de g} (final);


On se convaincra plus facilement en utilisant la fonction :code:`id` qui renvoie l'emplacement où est stocké un objet en mémoire et l'opérateur :code:`is` qui teste si deux objets sont physiquement égaux (c'est-à-dire s'ils occupent le même emplacement en mémoire).

.. ipython:: python

    def f(x):
        print('x début fonction f', id(x), x is a)
        x += 1
        print('x fin fonction f', id(x), x is a)


.. ipython:: python

    a = 2
    print('a avant appel fonction f', id(a))
    f(a)
    print('a après appel fonction f', id(a))
    a

.. ipython:: python

    def g(li):
        print('li début fonction g', id(li), lst is li)
        li.append('toto')
        print('li fin fonction g', id(li), lst is li)

.. ipython:: python

    lst = [1, 2, 3]
    print('lst avant appel fonction g', id(lst))
    g(lst)
    print('lst après appel fonction g', id(lst))
    lst

.. todo:: Faire un dessin

Finalement, on peut résumer les choses de la manière suivante.

.. tip::

    Un objet mutable peut-être modifé s'il est passé en argument à une fonction alors que ce ne sera jamais le cas pour un objet immutable.


.. todo:: Une variable globale ne peut pas être un paramètre si mot-clé global.

Une fonction est un objet
=========================

Il est important de noter qu'en Python, les fonctions sont des objets commes les autres (entiers, tuples, ...). Notamment, une fonction possède un type.

.. ipython:: python

    def f(x):
        return 2*x

    type(f)

Ceci est important car on peut par exemple utiliser une fonction comme un argument d'une autre fonction.

.. ipython:: python

    def appliquer(f, x):
        return f(x)

    def f(x):
        return 2*x

    appliquer(f, 5)

On peut également créer une fonction qui renvoie une autre fonction.

.. ipython:: python

    def multiplier_par(a):
        def f(x):
            return a*x
        return f

    multiplier_par(2)(5)


Fonctions anonymes
==================

En mathématiques, on peut parler d'une fonction de plusieurs manières.

    * On peut lui donner un nom : on peut par exemple considérer la fonction :math:`f` telle que :math:`f(x)=x^2`.
    * Mais si on ne compte pas réutiliser plus tard cette fonction, on peut tout simplement parler de la fonction :math:`x\mapsto x^2`.

De la même manière, on peut nommer explicitement une fonction.

::

    def f(x):
        return x**2

On peut également utiliser une *fonction anonyme* (également appelée *fonction lambda*).

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


Les fonctions anonymes sont limitées par rapport aux fonctions classiques : elles ne peuvent pas exécuter plusieurs instructions puisque seule **une** expression est renvoyée. Quel est alors l'intérêt des fonctions anonymes ? Il s'agit de créer des fonctions à usage unique qui peuvent notamment servir d'arguments dans d'autres fonctions.

Par exemple, Python dispose d'une fonction :code:`map` qui permet d'appliquer une fonction à chaque élément d'un objet de type itérable.

.. ipython:: python

    list(map(lambda x: 2*x, [1, 2, 3]))   # la fonction map renvoie un objet de type map qu'on convertit en liste

Bien entendu, on arriverait plus aisément au même résultat grâce à une liste en compréhension.

.. ipython:: python

    [2*x for x in [1, 2, 3]]

.. [#fctanonyme] Une fonction anonyme peut également être employée pour accomplir une action plutôt que pour renvoyer un objet.

    .. ipython:: python

        f = lambda li: li.append('toto')
        a = [1, 2]
        f(a)
        a               # La fonction anonyme f a modifié la liste a
        print(f(a))     # Par contre, la fonction ne renvoie rien (en fait, renvoie None)


.. todo:: Documentation d'une fonction
.. todo:: parler des effets de bord ???

.. todo:: définir une fonction à l'intérieur d'une autre fonction

.. todo:: named parameters
.. todo:: paramètre par défaut (cas d'un paramètre par défaut mutable)
