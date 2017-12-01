======================
Preuve d'un algorithme
======================


*Prouver* un algorithme signifie démontrer qu'un algorithme effectue bien la tâche qui lui est demandée.

Terminaison
===========

Il s'agit de montrer que l'algorithme se termine bien. La question se pose notamment lorsque l'algorithme comporte une boucle conditionnelle :code:`while`. La plupart du temps, cela revient à montrer qu'une quantité entière positive décroît strictement à chaque itération de la boucle (une suite d'entiers naturels strictement décroissante est nécessairement *finie*). Cette quantité est généralement appelé le **variant**.

On peut par exemple étudier l'algorithme d'Euclide pour le calcul du pgcd.

.. code-block:: python

    def pgcd(a, b):
      while b!= 0:
          a, b = b, a % b
      return a

On suppose que l'argument :code:`b` est un entier naturel. En notant :math:`b_k` la valeur de :code:`b` à la fin de la :math:`k^\text{ème}` itération (:math:`b_0` désigne la valeur de :code:`b` avant d'entrer dans la boucle), on a :math:`0\leq b_{k+1}<b_k` si :math:`b_k>0`. La suite :math:`(b_k)` est donc une suite strictement décroissante d'entiers naturels : elle est finie et la boucle se termine.


Correction
==========


Il s'agit de savoir si l'algorithme fournit bien la réponse attendue. Si l'algorithme comporte une boucle, on recherche généralement une quantité ou une propriété qui ne change pas au cours des itérations : on parle d\\'**invariant de boucle**.

A nouveau, on peut étudier l'algorithme d'Euclide.

.. code-block:: python

    def pgcd(a, b):
      while b!= 0:
          a, b = b, a % b
      return a

On note :math:`a_k` et :math:`b_k` les valeurs de :code:`a` et :code:`b` à la fin de la :math:`k^\text{ème}` itération (:math:`a_0` et :math:`b_0` désignent les valeurs de :code:`a` et :code:`b` avant d'entrer dans la boucle). Or, si :math:`a=bq+r`, il est clair que tout diviseur commun de :math:`a` et :math:`b` est un diviseur commun de :math:`b` et :math:`r` et réciproquement. Notamment, :math:`a\wedge b=b\wedge r`. Ceci prouve que :math:`a_k\wedge b_k=a_{k+1}\wedge b_{k+1}`. La quantité :math:`a_k\wedge b_k` est donc bien un invariant de boucle. En particulier, à la fin de la dernière itération (numérotée :math:`N`), :math:`b_N=0` de sorte que :math:`a_0\wedge b_0=a_N\wedge b_N=a_N\wedge0=a_N`. La fonction :code:`pgcd` renvoie donc bien le pgcd de :code:`a` et :code:`b`.
