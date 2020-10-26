# solveurEquations2ndDegre
Un projet réalisé en python, dont le but est de créer un programme qui résout des équations jusqu'au degré 2.

Pour l'utiliser, il faut appeler resolveurEquationsSimples.py en ligne de commande en lui fournissant en paramètre l'équation à résoudre sous forme de chaîne de caractères.
L'équation doit posséder une syntaxe du genre : "nb1 * X^2 + nb2 * X + nb3 = nb4 * X^2 + nb5 * X + nb6". (Les erreurs de saisies n'ont pas encore été gérées dans ce projet, il est donc important que, par exemple, les "X" soient en majuscule ou qu'il y ait des espaces entre les opérandes)


Le projet se constitue :

-d'un fichier de fonctions ("functions.py") permettant la manipulation de la chaîne de caractère contenant l'équation ainsi que des fonctions de calcul pour les résultats de cette équation.
-d'un fichier principal appelant les fonctions et retournant le résultat de l'équation. (resolveurEquationsSimples.py)
-d'un fichier contenant les tests des différentes fonctions. (tests.py)
