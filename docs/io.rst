=============
Entrée/sortie
=============

Un programme informatique doit souvent pouvoir interagir avec l'extérieur. Il existe plusieurs manières de faire cela :

* soit en interagissant directement avec l'utilisateur : celui-ci peut rentrer des données grâce au clavier ou voir le résultat du programme s'afficher à l'écran ;
* soit au moyen de fichiers : le programme peut lire des informations dans des fichiers ou au contraire écrire des résultats dans des fichiers.


Interaction directe avec l'utilisateur
======================================

L'interpéteur **IPython** affiche par défaut le résultat d'une expression non évaluée à :code:`None`. Ce n'est pas le cas lorsque l'on exécute un script Python. Si l'on veut afficher des résultats à l'écran, il faut explicitement utiliser la fonction :code:`print`.

Dans cet exemple, on exécute le script stocké dans le fichier :file:`script_print.py`.

.. literalinclude:: script_print.py

.. command-output:: python script_print.py

Inversement lorsque l'on souhaite demander une information à l'utilisateur, on utilise la fonction :code:`input`. Celle-ci interrompt l'exécution du programme, ce qui permet à l'utilsateur d'entrer des caractères au clavier. Pour terminer sa saisie, l'utilisateur appuie alors sur la touche :kbd:`Entrée`. La fonction :code:`input` renvoie alors la chaîne de caractères entrée par l'utilisateur et l'exécution du programme reprend son cours. On peut également fournir en argument optionnel à la fonction :code:`input` un message à destination de l'utilisateur qui sera affiché avant que celui-ci commence à saisir des caractères au clavier.

.. ipython:: python

    @suppress
    import sys
    @suppress
    from io import StringIO
    @suppress
    old = sys.stdin
    @suppress
    sys.stdin = StringIO('Toto')

    result = input('Quel est votre nom ?')

    @suppress
    sys.stdin = old

    # Ici l'utilisateur a entré Toto
    result

Fichiers
========

Pour ouvrir un fichier, on utilise la fonction :code:`open` en donnant en argument le chemin du fichier. On peut préciser plusieurs paramètres optionnels.

:code:`mode`
    **Mode d'ouverture** du fichier : essentiellement :code:`'r'` pour lecture, :code:`'w'` pour écriture et :code:`'r+'` pour lecture/écriture. Par défaut, un fichier est ouvert en lecture seulement.

:code:`encoding`
    **Encodage** [#encodage]_ du fichier : de nombreux encodages sont disponibles comme :code:`'utf8'` (à privilégier) ou :code:`'ascii'`.


.. ipython:: python

    f = open('test.txt', mode='r', encoding='utf8')
    f
    type(f)

.. warning::

    Le mode d'écriture :code:`'w'` crée un nouveau fichier si un fichier du même nom n'existe pas mais "écrase" un fichier existant dans le cas contraire.

L'objet renvoyé par open dispose d'une méthode :code:`close` pour fermer le fichier. On ne pourra alors plus lire ou écrire dedans.

.. ipython:: python

    f.close()

L'objet renvoyé par :code:`open` dispose de plusieurs méthodes permettant de lire ou d'écrire dans le fichier ouvert.

On utilisera pour les exemples le fichier :file:`test.txt` suivant.

.. literalinclude:: test.txt
    :language: text

Dans les exemples suivants, le caractère :code:`\n` désigne un *retour à la ligne*.

.. ipython:: python

    f = open('test.txt', mode='r', encoding='utf8')
    # Renvoie l'intégralité d'un fichier
    f.read()
    f.close()
    f = open('test.txt', mode='r', encoding='utf8')
    # Renvoie la liste des lignes
    f.readlines()
    f.close()
    f = open('toto.txt', mode='w', encoding='utf8')
    f.write("Ce qui se conçoit bien s'énonce clairement\n")
    f.write("Et les mots pour le dire viennent aisément.\n")
    f.close()

On vérifie que le fichier :file:`toto.txt` a bien été créé et que son contenu correspond bien à ce qu'on y a écrit.

.. literalinclude:: toto.txt
    :language: text

.. [#encodage] Un fichier n'est qu'une suite de bits stocké en mémoire. L'encodage permet de transformer cette suite de bits en une suite de caractères et inversement. C'est en quelque sorte une table qui à une suite de bits associe un caractère. Il faut connaître l'encodage d'un fichier texte pour pouvoir le lire correctement. Certains encodages ne permettent pas de représenter certains caractères. C'est pour cela qu'on préconise l'utilisation de l'encodage UTF-8 qui permet de représenter tous les caractères relatifs à chacune des langues de la planète.
