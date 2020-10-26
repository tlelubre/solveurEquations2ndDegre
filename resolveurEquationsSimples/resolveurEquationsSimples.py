"""
Résolution d'une équation allant jusqu'au degré 2.

Forme des opérantes des équations :
    Degré 0 -> a
    Degré 1 -> aX + b
    Degré 2 -> aX^2 + bX + c

    avec a,b,c étant des nombres réels.

"""


import functions
import sys # Module de manipulation du système.
import math # Module contenant des outils mathématiques.

equation = sys.argv[1] # Récupérer l'équation à résoudre.
equation1, equation2 = equation.split("=") # La diviser en deux équations selon le signe "=".

# Listing des différentes opérandes composant les équations.

# --- Pour l'équation 1.
operandesEq1 = functions.determinerOperandes(equation1)
liste1Constantes, liste1D1, liste1D2 = functions.trierOperandes(operandesEq1)
result1Const, result1D1, result1D2 = functions.extrairePartieEntiere(liste1D2, liste1D1, liste1Constantes)


# --- Pour l'équation 2.
operandesEq2 = functions.determinerOperandes(equation2)
liste2Constantes, liste2D1, liste2D2 = functions.trierOperandes(operandesEq2)
result2Const, result2D1, result2D2 = functions.extrairePartieEntiere(liste2D2, liste2D1, liste2Constantes)

# Simplification de l'équation de base.
resultD2 = result1D2 - result2D2
resultD1 = result1D1 - result2D1
resultConst = result1Const - result2Const

print("L\'équation simplifiée est :", "{0}X^2 + {1}X + {2}".format(resultD2, resultD1, resultConst))

# Déterminer le dégré de l'équation simplifiée.
degre = 0
if (resultD2 != 0):
    degre = 2
elif (resultD1 != 0):
    degre = 1

# En fonction du degré de l'équation, utiliser une méthode de résolution.

if degre > 2:
    print("The polynomial degree is strictly greater than 2, I can\'t solve the equation.")
elif degre == 2:
    functions.resoudreD2(resultConst, resultD1, resultD2)
elif degre == 1:
    functions.solution = resoudreD1(resultConst, resultD1)





    


                



