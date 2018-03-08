=========
Fonctions
=========

Une fonction est un bloc d'instructions que l'on peut appeler à tout moment d'un programme. Les fonctions ont plusieurs intérêts, notamment :

    * la réutilisation du code : éviter de répéter les mêmes séries d'instructions à plusieurs endroits d'un programme ;
    * la modularité : découper une tâche complexe en plusieurs sous-tâches plus simples.



Définir une fonction
====================

Au cours des chapitres précédents, on a déjà rencontré de nombreuses fonctions telles que :code:`print` ou :code:`len`. Chacune de ces fonctions reçoit un argument et effectue une action (la fonction :code:`print` affiche un objet à l'écran) ou renvoie une valeur (la fonction :code:`len` renvoie la taille d'un itérable).

Jusqu'à maintenant, on s'est contenté de faire appel à des fonctions prédéfinies. Mais on peut également définir ses propres fonctions : il faut alors **déclarer** ces fonctions avant de les utiliser. De manière générale, la syntaxe d'une déclaration de fonctions est la suivante.

::

    def <nom_fonction>(<paramètres>):   # En-tête de la fonction
        <instruction1>
        <instruction2>                  # Corps de la fonction
        ...
        return <valeur>

On décrit dans le *corps* de la fonction les traitements à effectuer sur les paramètres et on spécifie la valeur que doit renvoyer la fonction.

Considérons l'exemple simple suivant.

.. ipython:: python

    def factorielle(n):
        a = 1
        for k in range(1, n+1):
            a *= k
        return a

La fonction :code:`factorielle` prend en argument un objet :code:`n` (que l'on supposera être un entier naturel), calcule la factorielle de :code:`n` à l'aide d'une variable :code:`a` et renvoie cette valeur.

On constate que rien ne se passe lorsque la fonction est déclarée. Il faut **appeler** la fonction en fournissant une valeur à l'entier :code:`n` pour que le code soit exécuté.

.. ipython:: python

    factorielle(5)
    factorielle(7)

.. note::

    Il faut bien faire la différence entre **la déclaration** et **l'appel** de la fonction. Lorsqu'une fonction est **déclarée**, aucun code n'est exécuté. Il faut **appeler** la fonction pour que le code soit exécuté.

L'instruction :code:`return`
============================

On "sort" de la fonction dès qu'on recontre une instruction :code:`return` : en particulier, les instructions suivant un :code:`return` ne sont pas exécutées.

.. ipython:: python

    def test(n):
        if n % 2 == 0:
            return "n est un multiple de 2"
        if n % 3 ==0:
            return "n est un multiple de 3"
        return "Bidon"

    test(4)
    test(9)
    test(6)
    test(11)

On peut cependant utiliser ceci à notre avantage : par exemple, pour sortir d'une boucle :code:`for` avant d'avoir accompli toutes les itérations.

.. ipython:: python

    from math import sqrt, floor

    def est_premier(n):
        if n <= 1:
            return False
        for d in range(2, floor(sqrt(n)) + 1):
            if n % d == 0:
                return False
        return True

    print([(n, est_premier(n)) for n in range(10)])

Une fonction peut ne pas contenir d'instruction :code:`return` ou peut ne renvoyer aucune valeur. En fait, si on ne renvoie pas explicitement de valeur, Python renverra par défaut la valeur particulière :code:`None`.

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


.. todo:: on peut déclarer une fonction dans une autre fonction.


Paramètres et arguments
=======================

Une fonction peut avoir zéro, un ou plusieurs paramètres [#zeroargument]_.

.. note:: Bien que les termes *paramètres* et *arguments* soient souvent confondus, il existe une nuance dont nous tiendrons compte dans ce chapitre : les *paramètres* sont les noms intervenant dans l'en-tête de la fonction tandis que les *arguments* sont les valeurs passées à la fonction lors de son appel.

    .. ipython:: python

        def add(a, b):      # Les paramètres sont a et b
            return a + b

        add(5, 10)          # Les arguments sont 5 et 10

De même que pour les variables, les noms des paramètres doivent refléter leur utilisation pour que le code soit plus lisible. Par ailleurs, on peut passer des arguments à une fonction en utilisant les noms des paramètres, ce qui rend le code encore plus explicite.

.. ipython:: python

    def nom_complet(prenom, nom):
        return prenom[0].upper() + prenom[1:].lower() + ' ' + nom.upper()

    nom_complet(prenom='james', nom='bond')

L'emploi d\\'*arguments nommés* permet de passer les arguments dans un ordre différent de l'ordre des paramètres dans l'en-tête de la fonction.

.. ipython:: python

    nom_complet(nom='PrOuSt', prenom='MARcel')

Il est possible de donner des valeurs par défaut aux paramètres d'une fonction : les arguments correspondants ne sont plus alors requis lors de l'appel de la fonction.

.. ipython:: python

    def nom_complet(prenom='Joe', nom='Bob'):
        return prenom[0].upper() + prenom[1:].lower() + ' ' + nom.upper()

    nom_complet()
    nom_complet('ulysse')
    nom_complet(nom='capet')

Dans l'en-tête d'une fonction les paramètres avec des valeurs par défaut doivent toujours *suivre* les paramètres sans valeurs par défaut sous peine de déclencher une erreur de syntaxe.

.. ipython:: python

    def toto(a=1, b, c=2):
        pass

Le but est d'éviter toute ambiguïté. En effet, quels seraient les arguments passés lors de l'appel de fonction :code:`toto(5, 6)` ? :code:`a=1`, :code:`b=5` et :code:`c=6` ou bien :code:`a=5`, :code:`b=6` et :code:`c=2` ?

.. todo:: arguments par défaut mutables


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

    De manière générale, il est plutôt déconseillé d'utiliser des variables globales à l'intérieur d'une fonction. Il est par exemple plus difficile de tester ou débugger une fonction faisant appel à des variables globales : en plus de chercher les bugs à l'intérieur de la fonction, il faudra examiner tous les endroits où ces variables globales sont potentiellement modifiées, ce qui peut devenir un vrai casse-tête dans un programme complexe.

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
        return None

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

    f(5)


On ne peut pas accéder à des variables locales à l'extérieur de la fonction où elles sont définies.

.. ipython:: python

    def f():
        c = 2
        return None

    f()
    c   # c est inconnu à l'extérieur de la fonction


On peut donc également voir les variables locales comme des variables *temporaires* dont l'existence n'est assurée qu'à l'intérieur de la fonction où elles interviennent.

On peut néanmoins modifier une variable globale à l'intérieur d'une fonction : on utilise alors le mot-clé :code:`global`.

.. ipython:: python

    a = 1
    def f():
        global a
        a = 2
        return None

    a
    f()
    a   # a vaut bien 2


Les paramètres d'une fonction ont également une portée locale.

.. ipython:: python

    def f(c):
        return 2 * c

    c   # c est inconnu à l'extérieur de la fonction


Fonctions et mutabilité
=======================

Considérons ce premier exemple où l'argument est un entier.

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


Effets de bord
==============

En plus de renvoyer une valeur, une fonction peut entraîner des modifications au-delà de sa portée comme :

* modifier des variables globales ;
* modifier des arguments mutables ;
* afficher des informations à l'écran ;
* enregistrer des données dans un fichier.

On parle alors d\\'**effet de bord**. Les effets de bord sont à utiliser avec parcimonie : en effet,


Une fonction est un objet
=========================

Il est important de noter qu'en Python, les fonctions sont des objets commes les autres (entiers, tuples, ...). Notamment, une fonction possède un type.

.. ipython:: python

    def f(x):
        return 2 * x

    type(f)

Ceci est important car on peut par exemple utiliser une fonction comme un argument d'une autre fonction.

.. ipython:: python

    def appliquer(f, x):
        return f(x)

    def f(x):
        return 2 * x

    appliquer(f, 5)

On peut également créer une fonction qui renvoie une autre fonction.

.. ipython:: python

    def multiplier_par(a):
        def f(x):
            return a * x
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
    f = lambda x: x**2              # On peut bien sûr donner un nom à une fonction anonyme
    f(4)
    g = lambda x, y: x**2 + y**2    # Une fonction anonyme peut avoir plus d'un argument
    g(1, 2)


De manière générale, la syntaxe d'une fonction anonyme est la suivante.

::

    lambda <paramètres>: <expression>

A la différence d'une fonction classique, une fonction anonyme ne nécessite pas d'instruction :code:`return` : l'expression suivant :code:`:` est renvoyée [#fctanonyme]_.


Les fonctions anonymes sont limitées par rapport aux fonctions classiques : elles ne peuvent pas exécuter plusieurs instructions puisque seule **une** expression est renvoyée. Quel est alors l'intérêt des fonctions anonymes ? Il s'agit de créer des fonctions à usage unique qui peuvent notamment servir d'arguments dans d'autres fonctions.

Par exemple, Python dispose d'une fonction :code:`map` qui permet d'appliquer une fonction à chaque élément d'un objet de type itérable.

.. ipython:: python

    list(map(lambda x: 2*x, [1, 2, 3]))   # la fonction map renvoie un objet de type map qu'on convertit en liste

Bien entendu, on arriverait plus aisément au même résultat grâce à une liste en compréhension.

.. ipython:: python

    [2 * x for x in [1, 2, 3]]


.. rubric:: Notes

.. [#zeroargument] Une fonction sans paramètre nécessite quand même des parenthèses dans son en-tête.

    .. ipython:: python

        def f():
            return 1

        f()

.. [#fctanonyme] Une fonction anonyme peut également avoir des effets de bord.

    .. ipython:: python

        f = lambda li: li.append('toto')
        a = [1, 2]
        f(a)
        a               # La fonction anonyme f a modifié la liste a
        print(f(a))     # Par contre, la fonction ne renvoie rien (en fait, renvoie None)


.. todo:: Documentation d'une fonction

.. todo:: définir une fonction à l'intérieur d'une autre fonction
