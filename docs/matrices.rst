========
Matrices
========

Dans ce paragraphe, les matrices seront représentées par des listes de listes. Par exemple, la matrice :math:`\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}` sera représentée par la liste de listes :code:`[[1, 2, 3], [4, 5, 6]]` [#numpy_matrices]_.

Produit matriciel
=================


.. ipython:: python

    def produit(A, B):
        return [[sum(L[k] * B[k][j] for k in range(len(L))) for j in range(len(B[0]))] for L in A]

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5,6]]
    produit(A, B)
    produit(B, A)


Opérations élémentaires
=======================

On définit plusieurs opérations élémentaires sur les lignes d'une matrice.

- l'échange de lignes :math:`L_i\leftrightarrow L_j`

    .. ipython:: python

        def echange_lignes(M, i, j):
            M[i], M[j] = M[j], M[i]
            return M

- la transvection :math:`L_i\leftarrow L_i+\lambda L_j`

    .. ipython:: python

        def transvection_ligne(M, i, j, l):
            M[i] = [M[i][k] + l * M[j][k] for k in range(len(M[i]))]
            return M

- la dilatation :math:`L_i\leftarrow\lambda L_i`

    .. ipython:: python

        def dilatation_ligne(M, i, l):
            M[i] = [coeff * l for coeff in M[i]]
            return M

.. warning:: Les fonctions précédentes, modifient la matrice donnée en argument puisqu'une liste est un objet mutable.

Algorithme du pivot de Gauss
============================

A l'aide des opérations élémentaires précédemment définies, on peut alors définir une fonction appliquant l'algorithme du pivot de Gauss à une matrice pour la mettre sous forme *échelonnée*.

Pour des raisons de stabilité numérique, on recherche le pivot de valeur absolue maximale.

.. ipython:: python

    def recherche_pivot_lignes(M, i):
        m = abs(M[i][i])
        j = i
        for k in range(i + 1, len(M)):
            if abs(M[i][j]) > m:
                j = k
        return j

.. ipython:: python

    def pivot_lignes(M):
        for i in range(len(M)):
            j = recherche_pivot_lignes(M, i)
            if j != i:
                echange_lignes(M, i, j)
            if M[i][i] != 0:
                for j in range(i + 1, len(M)):
                    transvection_ligne(M, j, i, -M[j][i] / M[i][i])
        return M

.. note:: Le test :code:`if M[i][i] != 0:`, s'il est correct en théorie, est en fait ridicule en pratique. Puisque l'on ne travaille qu'avec des valeurs approchées, un pivot nul en théorie (si l'on effectuait des calculs exacts) ne sera jamais nul en pratique.

.. ipython:: python

    M = [[1, 2, 3, 4], [5, 6, 7, 8], [6, 8, 10, 12], [4, 4, 4, 4]]
    pivot_lignes(M)

.. note:: On pourrait alors utiliser la forme échelonnée pour calculer le rang d'une matrice : il suffirait alors de compter le nombre de lignes non nulles. Mais à nouveau, il n'est pas évident de savoir en pratique si une ligne est réellement nulle puisqu'on a accès qu'à des valeurs approchées de ses coefficients.

Résolution de systèmes linéaires
================================

On considère un **système de Cramer** sous forme matricielle :math:`AX=B` où :math:`A` est une matrice inversible, :math:`B` une matrice colonne donnée et :math:`X` une matrice colonne inconnue. Pour résoudre ce système, il suffit dans un premier temps de mettre la matrice :math:`\begin{pmatrix}A\mid B\end{pmatrix}` sous forme échelonnée. On peut utiliser la fonction :code:`pivot_lignes` précédemment définie mais on aura également besoin d'une fonction permettant de concaténer une matrice carrée (sous forme d'une liste de listes) et une matrice colonne (sous forme d'une liste).

.. ipython:: python

    def concatenation_vecteur(A, B):
        return [A[i] + [B[i]] for i in range(len(A))]

Une fois que le pivot de Gauss a été effectué sur la matrice :math:`\begin{pmatrix}A\mid B\end{pmatrix}`, il faut effectuer un pivot "à rebours" pour déterminer la solution du système :math:`AX=B`.

.. ipython:: python

    def pivot_lignes_rebours(M):
        for i in reversed(range(len(M))):
            dilatation_ligne(M, i, 1 / M[i][i])
            for j in range(i):
                transvection_ligne(M, j, i, -M[j][i])
        return M

La matrice colonne solution est alors la dernière colonne de la matrice obtenue, qu'il faut donc extraire.

.. ipython:: python

    def extract_vecteur(M):
        return [L[-1] for L in M]

On peut alors définir une fonction d'arguments une matrice inversible :math:`A` et une matrice colonne :math:`B` renvoyant l'unique solution du système :math:`AX=B`.

.. ipython:: python

    def resolution(A, B):
        M = concatenation_vecteur(A, B)
        pivot_lignes(M)
        pivot_lignes_rebours(M)
        return extract_vecteur(M)

.. ipython:: python

    A = [[1, -1, 2], [3, 2, 1], [2, -3, -2]]
    B = [5, 10, -10]
    resolution(A, B)


Inversion d'une matrice
=======================

On peut également utiliser l'algorithme du pivot de Gauss pour inverser une matrice : on transforme une matrice inversible en la matrice identité en effectuant l'algorithme du pivot de Gauss puis l'algorithme du pivot de Gauss "à rebours". On récpercute les opérations effectuées sur une matrice identité de même taille que :math:`A`, qui est alors transformée en l'inverse de la matrice initiale. Pour effectuer aissément les mêmes opérations sur les lignes d'une matrice :math:`A` et la matrice identité :math:`I`, on forme la matrice :math:`\begin{pmatrix}A\mid I\end{pmatrix}`.

.. ipython:: python

    def concat_identite(A):
        return [A[i] + [1 if j== i else 0 for j in range(len(A))] for i in range(len(A))]

Après les pivots, il reste à extraire la matrice inverse.

.. ipython:: python

    def extract_inverse(M):
        return [L[len(M):] for L in M]

On peut alors proposer la fonction suivante.

.. ipython:: python

    def inverse(A):
        M = concat_identite(A)
        pivot_lignes(M)
        pivot_lignes_rebours(M)
        return extract_inverse(M)

.. ipython:: python

    A = [[1, 5, 6], [2, 11, 19], [3, 19, 47]]
    B = inverse(A)
    B
    produit(A, B)
    produit(B, A)


Calcul du déterminant
=====================

On peut également se servir du pivot de Gauss pour calculer le déterminant d'une matrice carrée. En effet, le déterminant est invariant par transvection et échange de lignes et le déterminant d'une matrice triangulaire est le produit de ses coefficients diagonaux [#determinant_idiot]_.

.. ipython:: python

    def determinant(M):
        pivot_lignes(M)
        p = 1
        for i in range(len(M)):
            p *= M[i][i]
        return p

.. ipython:: python

    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    determinant(M)


.. [#numpy_matrices] Le module :code:`numpy` possède un type :code:`matrix` permettant de simplifier grandement les fonctions suivantes. Il possède d'ailleurs également un sous module :code:`numpy.linalg` regroupant de nombreuses fonctions ayant trait à l'algèbre linéaire sur les matrices.

.. todo:: mettre un lien vers chapitre numpy ?

.. [#determinant_idiot] On pourrait penser à calculer le déterminant via la formule qui l'exprime en fonction des coefficients de la matrice ou à l'aide d'un développement par rapport à une ligne ou une colonne mais on verra dans le chapitre ??? que c'est nettemment moins efficace que le pivot de Gauss

.. todo:: Mettre référence vers le chapitre complexité
