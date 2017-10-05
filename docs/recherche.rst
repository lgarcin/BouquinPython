========================
Algorithmes de recherche
========================



Recherche d'un élément dans une liste
=====================================


Il faut noter que Python dispose déjà de l'opérateur :code:`in` pour tester si un élément figure dans une liste.

.. ipython:: python

    2 in [5, 4, 1, 2, 3]
    6 in [5, 4, 1, 2, 3]

La méthode :code:`index` permet de renvoyer l'indice de l'élément dans la liste s'il a été trouvé.

.. ipython:: python

    [5, 4, 1, 2, 3].index(2)
    [5, 4, 1, 2, 3].index(6)



On peut néanmoins proposer notre propre algorithme : il suffit de balayer la liste et de renvoyer :code:`True` dès qu'on trouve l'élément recherché et :code:`False` si on a parcouru toute la liste sans trouver l'élément.

.. ipython:: python

    def appartient(elt, lst):
        for e in lst:
            if e == elt:
                return True
        return False

    appartient(2, [5, 4, 1, 2, 3])
    appartient(6, [5, 4, 1, 2, 3])

On peut également proposer une version qui renvoie l'indice la première occurence de l'élément recherché s'il est trouvé et :code:`None` sinon.

.. ipython:: python

    def indice(elt, lst):
        for i in range(len(lst)):
            if lst[i] == elt:
                return i
        return None

    indice(2, [5, 4, 1, 2, 3])
    indice(6, [5, 4, 1, 2, 3])  # L'interpréteur IPython n'affiche pas None



Recherche d'un élément dans une liste triée
===========================================

Lorsque l'on dispose d'une liste triée par ordre croissant, on peut grandement améliorer notre algorithme en utilisant le principe de **dichotomie**.

* On recherche tout d'abord l'élément central de la liste.
* Si c'est l'élément recherché, on s'arrête. Sinon, on le compare à l'élément recherché.
* Si l'élément recherché est inférieur à l'élément central, on le recherche dans la première partie de la liste. Sinon, on le recherche dans la deuxième partie de la liste.
* On retourne donc à la première étape de notre algorithme appliqué à l'une des deux demi-listes.

.. ipython:: python

    def appartient_dicho(elt, lst):
        g = 0
        d = len(lst) - 1
        while g <= d:
            m = (g + d) // 2
            if lst[m] == elt:
                return True
            if elt < lst[m]:
                d = m - 1
            else:
                g = m + 1
        return False

    appartient_dicho(13, [1, 3, 5, 7, 8, 10, 13, 14, 17, 19])
    appartient_dicho(18, [1, 3, 5, 7, 8, 10, 13, 14, 17, 19])

Comme souvent, un dessin vaut mieux qu'un long discours. On donne deux exemples d'application de cet algorithme.

.. rubric:: Recherche de :code:`5` dans la liste :code:`[1, 3, 5, 7, 8, 10, 13, 14, 17, 19, 20]`

.. tikz::
    :libs: matrix

    \tikzset{g/.style={fill=gray!10,draw}}
    \tikzset{b/.style={fill=blue!10,draw}}
    \tikzset{r/.style={fill=red!10,draw}}
    \tikzset{t/.style={fill=green!10,draw}}
    \tikzset{every node/.style={text height=1.5ex, text depth=.25ex}}
    \matrix[matrix of nodes, row sep=4em, nodes = {minimum width = 2em, minimum height = 2em}](recherche){
        |[b]|1 & |[b]|3 & |[b]|5 & |[b]|7 & |[b]|8 & |[r]|10 & |[b]|13 & |[b]|14 & |[b]|17 & |[b]|19 & |[b]|20\\
        |[b]|1 & |[b]|3 & |[t]|5 & |[b]|7 & |[b]|8 & |[g]|10 & |[g]|13 & |[g]|14 & |[g]|17 & |[g]|19 & |[g]|20\\
    };
    \node[below of=recherche-1-1](g1){\tt g};
    \draw[->](g1)--(recherche-1-1);
    \node[below of=recherche-1-11](d1){\tt d};
    \draw[->](d1)--(recherche-1-11);
    \node[above of=recherche-1-6](m1){\tt m};
    \draw[->](m1)--(recherche-1-6);

    \node[below of=recherche-2-1](g2){\tt g};
    \draw[->](g2)--(recherche-2-1);
    \node[below of=recherche-2-5](d2){\tt d};
    \draw[->](d2)--(recherche-2-5);
    \node[above of=recherche-2-3](m2){\tt m};
    \draw[->](m2)--(recherche-2-3);


.. rubric:: Recherche de :code:`13` dans la liste :code:`[1, 3, 5, 7, 8, 10, 13, 14, 17, 19]`

.. tikz::
    :libs: matrix

    \tikzset{g/.style={fill=gray!10,draw}}
    \tikzset{b/.style={fill=blue!10,draw}}
    \tikzset{r/.style={fill=red!10,draw}}
    \tikzset{t/.style={fill=green!10,draw}}
    \tikzset{every node/.style={text height=1.5ex, text depth=.25ex}}
    \matrix[matrix of nodes, row sep=4em, nodes = {minimum width = 2em, minimum height = 2em}](recherche){
        |[b]|1 & |[b]|3 & |[b]|5 & |[b]|7 & |[r]|8 & |[b]|10 & |[b]|13 & |[b]|14 & |[b]|17 & |[b]|19\\
        |[g]|1 & |[g]|3 & |[g]|5 & |[g]|7 & |[g]|8 & |[b]|10 & |[b]|13 & |[r]|14 & |[b]|17 & |[b]|19\\
        |[g]|1 & |[g]|3 & |[g]|5 & |[g]|7 & |[g]|8 & |[r]|10 & |[b]|13 & |[g]|14 & |[g]|17 & |[g]|19\\
        |[g]|1 & |[g]|3 & |[g]|5 & |[g]|7 & |[g]|8 & |[g]|10 & |[t]|13 & |[g]|14 & |[g]|17 & |[g]|19\\
    };
    \node[below of=recherche-1-1](g1){\tt g};
    \draw[->](g1)--(recherche-1-1);
    \node[below of=recherche-1-10](d1){\tt d};
    \draw[->](d1)--(recherche-1-10);
    \node[above of=recherche-1-5](m1){\tt m};
    \draw[->](m1)--(recherche-1-5);

    \node[below of=recherche-2-6](g2){\tt g};
    \draw[->](g2)--(recherche-2-6);
    \node[below of=recherche-2-10](d2){\tt d};
    \draw[->](d2)--(recherche-2-10);
    \node[above of=recherche-2-8](m2){\tt m};
    \draw[->](m2)--(recherche-2-8);

    \node[below of=recherche-3-6](g3){\tt g};
    \draw[->](g3)--(recherche-3-6);
    \node[below of=recherche-3-7](d3){\tt d};
    \draw[->](d3)--(recherche-3-7);
    \node[above of=recherche-3-6](m3){\tt m};
    \draw[->](m3)--(recherche-3-6);

    \node[below of=recherche-4-7](gd){\tt{g=d}};
    \draw[->](gd)--(recherche-4-7);
    \node[above of=recherche-4-7](m4){\tt m};
    \draw[->](m4)--(recherche-4-7);




A nouveau, on peut proposer une version qui renvoie l'indice de la première occurence de l'élément recherché plutôt qu'un booléen.

.. ipython:: python

    def indice_dicho(elt, lst):
        g = 0
        d = len(lst) - 1
        while g <= d:
            m = (g + d) // 2
            if lst[m] == elt:
                return m
            if elt < lst[m]:
                d = m - 1
            else:
                g = m + 1
        return None

    indice_dicho(13, [1, 3, 7, 8, 10, 13, 14, 17, 19])
    indice_dicho(18, [1, 3, 7, 8, 10, 13, 14, 17, 19])  # L'interpréteur IPython n'affiche pas None

.. rubric:: Comparaison de l'efficacité des deux algorithmes

On peut comparer les temps de calcul des deux versions de l'algorithme de recherche d'un élément grâce à la *commande magique* :code:`%timeit` : celle-ci permet d'exécuter un grand nombre de fois la même instruction et de mesurer le temps d'exécution moyen de cette instruction.

.. .. ipython:: python
..
..     from numpy.random import randint    # La fonction randint permet de générer des entiers de manière aléatoire
..     for N in 100, 1000, 10000, 100000:
..         lst = [k for k in range(N)]     # On crée une liste d'entiers triée par ordre croissant
..         print(N,"éléments")
..         print("Recherche standard")
..         %timeit appartient(randint(N), lst)
..         print("Recherche par dichotomie")
..         %timeit appartient_dicho(randint(N), lst)
..         print("\n")

On remarque en particulier que le temps de calcul avec l'algorithme standard augmente à peu près proportionnellement à la taille de la liste tandis que le temps de calcul avec l'algorithme par dichotomie augmente très peu avec la taille de la liste. Le gain de temps de calcul est donc d'autant plus grand que la liste est grande [#pasdemiracle]_. On donnera une comparaison quantitative de ces deux temps de calcul dans le chapitre sur la complexité.

.. todo:: mettre un lien vers complexité

.. .. plot::
..
..     from matplotlib.pyplot import plot
..     plot([4, 3, 2])
..
..
.. .. ipython:: python
..
..     val = []
..     lst = [k for k in range(N)]
..     for n in range(1, N, 10000):
..         print(n)
..         a = %timeit -o appartient(randint(n), lst[:n])
..         val.append(a.average)
..
.. .. ipython:: python
..
..     from matplotlib.pyplot import plot
..     val
..     @savefig recherche.png width=4in
..     plot(val)
..
..
..
.. .. ipython:: python
..
..     val = []
..     lst = [k for k in range(N)]
..     for n in range(1, N, 10000):
..         print(n)
..         a = %timeit -o appartient_dicho(randint(n), lst[:n])
..         val.append(a.average)
..
.. .. ipython:: python
..
..     from matplotlib.pyplot import plot
..     val
..     @savefig recherche_dicho.png width=4in
..     plot(val)


Recherche d'une sous-chaîne dans une chaîne de caractères
=========================================================

L'objectif est de retrouver une sous-chaîne (qu'on appellera *motif*) dans une chaîne de caractères. Par exemple, la chaîne :code:`"pitapipapa"` contient le motif :code:`"pipa"` mais pas le motif :code:`"tapi"`. Python propose déjà cette fonctionnalité à l'aide de l'opérateur :code:`in`.

.. ipython:: python

    "pipa" in "pitapipapa"
    "tapa" in "pitapipapa"

La méthode :code:`index` permet de renvoyer l'indice du caractère où a été trouvé le motif le cas échéant.

.. ipython:: python

    "pitapipapa".index("pipa")
    "pitapipapa".index("tapa")


On présente ici un algorithme naïf qui est assez peu efficace mais qui a le mérite d'être très facile à comprendre : on prend successivement chaque caractère de la chaîne comme point de départ et on compare les caractères de la chaîne et les caractères du motif à partir de ce point de départ.


.. ipython:: python

    def recherche_chaine(chaine, motif):
        n = len(chaine)
        m = len(motif)
        for ind in range(n-m):
            nb = 0
            while nb < m and chaine[ind+nb] == motif[nb]:
                nb +=1
            if nb == m:
                return True
        return False

    recherche_chaine("pitapipapa", "pipa")
    recherche_chaine("patapipapa", "tapa")


.. rubric:: Recherche du motif :code:`"pipa"` dans la chaîne :code:`"pitapipapa"`

.. tikz::
    :libs: matrix

    \tikzset{g/.style={fill=gray!10,draw}}
    \tikzset{b/.style={fill=blue!10,draw}}
    \tikzset{r/.style={fill=red!10,draw}}
    \tikzset{t/.style={fill=green!10,draw}}
    \tikzset{s/.style={font=\bf}}
    \tikzset{every node/.style={text height=1.5ex, text depth=.25ex}}
    \matrix[matrix of nodes, nodes = {minimum width = 1.5em, minimum height = 1.5em}](recherche){
        |[s,t]|p & |[g]|i & |[g]|t & |[g]|a & |[g]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[s,t]|p & |[t]|i & |[g]|t & |[g]|a & |[g]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[s,t]|p & |[t]|i & |[r]|t & |[g]|a & |[g]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[s,r]|i & |[g]|t & |[g]|a & |[g]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[g]|i & |[s,r]|t & |[g]|a & |[g]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[g]|i & |[g]|t & |[s,r]|a & |[g]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[g]|i & |[g]|t & |[g]|a & |[s,t]|p & |[g]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[g]|i & |[g]|t & |[g]|a & |[s,t]|p & |[t]|i & |[g]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[g]|i & |[g]|t & |[g]|a & |[s,t]|p & |[t]|i & |[t]|p & |[g]|a & |[g]|p & |[g]|a\\
        |[g]|p & |[g]|i & |[g]|t & |[g]|a & |[s,t]|p & |[t]|i & |[t]|p & |[t]|a & |[g]|p & |[g]|a\\
    };
    \node[right of=recherche-1-10, anchor=west]{\tt{ind=0, nb=1}};
    \node[right of=recherche-2-10, anchor=west]{\tt{ind=0, nb=2}};
    \node[right of=recherche-3-10, anchor=west]{\tt{ind=0, nb=2}};
    \node[right of=recherche-4-10, anchor=west]{\tt{ind=1, nb=0}};
    \node[right of=recherche-5-10, anchor=west]{\tt{ind=2, nb=0}};
    \node[right of=recherche-6-10, anchor=west]{\tt{ind=3, nb=0}};
    \node[right of=recherche-7-10, anchor=west]{\tt{ind=4, nb=1}};
    \node[right of=recherche-8-10, anchor=west]{\tt{ind=4, nb=2}};
    \node[right of=recherche-9-10, anchor=west]{\tt{ind=4, nb=3}};
    \node[right of=recherche-10-10, anchor=west]{\tt{ind=4, nb=4}};



On peut à nouveau proposer une version de l'algorithme qui renvoie l'indice de la *première occurence* rencontrée.

.. ipython:: python

    def indice_chaine(chaine, motif):
        n = len(chaine)
        m = len(motif)
        for ind in range(n-m):
            nb = 0
            while nb < m and chaine[ind+nb] == motif[nb]:
                nb +=1
            if nb == m:
                return nb
        return None

    indice_chaine("pitapipapa", "pipa")
    indice_chaine("patapipapa", "tapa")     # L'interpréteur IPython n'affiche pas None


.. rubric:: Notes

.. [#pasdemiracle] Il ne faut cependant pas crier tout de suite au miracle. L'algorithme de recherche par dichotomie nécessite que la liste traitée soit auparavant triée. Et le tri est une opération qui nécessite un certain temps de calcul (plus élevé que celui de l'algorithme de recherche standard).
