from functions import determinerOperandes
from functions import trierOperandes
from functions import extrairePartieEntiere
from functions import resoudreD1
from functions import resoudreD2


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------Tests-------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("######################################################")
print("Test de la fonction \"determinerOperandes(equation)\"")
print("######################################################")

equation = "2 * X^2 + 4 * X + 3"  # 3 types d'opérandes.
print("------------------------------------------------------------------------------------")
print("Test : 1 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "X^2 + 2 * X + 7" # Pas d'opérande constante.
print("------------------------------------------------------------------------------------")
print("Test : 2 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "X^2 + X + 3" # Valeur de 1 pour l'opérande en X² et en X.
print("------------------------------------------------------------------------------------")
print("Test : 3 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "4 * X + 3" # Pas d'opérande en X².
print("------------------------------------------------------------------------------------")
print("Test : 4 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "2 + 3 * X^2 + 4 * X" # Equation dont les opérandes ne sont pas ordonnées.
print("------------------------------------------------------------------------------------")
print("Test : 5 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "-2 * X^2 + 4 * X + 3"
print("------------------------------------------------------------------------------------")
print("Test : 6 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "-2 * X^2 - 4 * X + 3"
print("------------------------------------------------------------------------------------")
print("Test : 7 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "-27 * X^2 - 41 * X + 33"
print("------------------------------------------------------------------------------------")
print("Test : 8 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "-27  - 41 * X + 33" # Nombres à 2 chiffres et opérandes négatives.
print("------------------------------------------------------------------------------------")
print("Test : 9 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "-2.3  - 4.1 * X + 33" # Nombres à virgule et à 2 chiffres.
print("------------------------------------------------------------------------------------")
print("Test : 10 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "    X^2 + X + 1" # Espaces au début de l'équation.
print("------------------------------------------------------------------------------------")
print("Test : 11 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "X^2 + X + 1    " # Espaces en fin de l'équation.
print("------------------------------------------------------------------------------------")
print("Test : 12 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")

equation = "X^2 + 1" # Pas d'opérande en X.
print("------------------------------------------------------------------------------------")
print("Test : 13 : L\' équation est : ", equation)
print("Les opérandes sont : ", determinerOperandes(equation))
print("------------------------------------------------------------------------------------")



print("######################################################")
print("Test de la fonction \"trierOperandes(operandes)\"")
print("######################################################")

operandes = ["4X^2", "3X", "3X^2", "X", "4", "-4X^2"]
print("------------------------------------------------------------------------------------")
print("Test : 1 : Les opérandes sont : ", operandes)
print("Les opérandes triées par degré sont : ", trierOperandes(operandes))
print("------------------------------------------------------------------------------------")

operandes = ["3X", "X", "2X", "-4X"]
print("------------------------------------------------------------------------------------")
print("Test : 2 : Les opérandes sont : ", operandes)
print("Les opérandes triées par degré sont : ", trierOperandes(operandes))
print("------------------------------------------------------------------------------------")

operandes = ["-3X", "-X", "-2X", "-4X"]
print("------------------------------------------------------------------------------------")
print("Test : 3 : Les opérandes sont : ", operandes)
print("Les opérandes triées par degré sont : ", trierOperandes(operandes))
print("------------------------------------------------------------------------------------")

operandes = ["3X^2", "X^2", "2X^2", "-4X^2"]
print("------------------------------------------------------------------------------------")
print("Test : 4 : Les opérandes sont : ", operandes)
print("Les opérandes triées par degré sont : ", trierOperandes(operandes))
print("------------------------------------------------------------------------------------")

operandes = ["33X", "21X^2", "29X", "-41", "4"]
print("------------------------------------------------------------------------------------")
print("Test : 5 : Les opérandes sont : ", operandes)
print("Les opérandes triées par degré sont : ", trierOperandes(operandes))
print("------------------------------------------------------------------------------------")


print("#######################################################################################")
print("Test de la fonction \"extrairePartieEntiere(operandesD2, operandesD1, operandesConst)\"")
print("#######################################################################################")


# Des opérandes de chaque type et avec valeurs > 1.
operandesD2 = ["2X^2", "3X^2"]
operandesD1 = ["2X", "3X"]
operandesConst = ["2", "3"]
print("------------------------------------------------------------------------------------")
print("Test : 1 : Les listes d'opérandes sont : ", operandesD2, operandesD1, operandesConst)
print("Les opérandes résultantes sont : ", extrairePartieEntiere(operandesD2, operandesD1, operandesConst))
print("------------------------------------------------------------------------------------")

# Des opérandes de chaque type avec valeur 1 ou 0.
operandesD2 = ["X^2", "X^2"]
operandesD1 = ["X", "3X"]
operandesConst = ["1", "0"]
print("------------------------------------------------------------------------------------")
print("Test : 2 : Les listes d'opérandes sont : ", operandesD2, operandesD1, operandesConst)
print("Les opérandes résultantes sont : ", extrairePartieEntiere(operandesD2, operandesD1, operandesConst))
print("------------------------------------------------------------------------------------")


print("#######################################################################################")
print("Test de la fonction \"resoudreD1(constante, d1)\"")
print("#######################################################################################")


# Pour X = 1 et une constante positive.
constante = 5
d1 = 1
print("------------------------------------------------------------------------------------")
print("Test : 1 : Les opérandes sont {} pour la constante et {} pour la variable en X : ".format(constante, d1))
print(resoudreD1(constante, d1))
print("------------------------------------------------------------------------------------")

# Pour X = 1 et une constante négative.
constante = -5
d1 = 1
print("------------------------------------------------------------------------------------")
print("Test : 2 : Les opérandes sont {} pour la constante et {} pour la variable en X : ".format(constante, d1))
print(resoudreD1(constante, d1))
print("------------------------------------------------------------------------------------")

# Pour X != 1 et une constante positive.
constante = 5
d1 = 4
print("------------------------------------------------------------------------------------")
print("Test : 3 : Les opérandes sont {} pour la constante et {} pour la variable en X : ".format(constante, d1))
print(resoudreD1(constante, d1))
print("------------------------------------------------------------------------------------")

# Pour X != 1 et une constante négative.
constante = -5
d1 = 4
print("------------------------------------------------------------------------------------")
print("Test : 4 : Les opérandes sont {} pour la constante et {} pour la variable en X : ".format(constante, d1))
print(resoudreD1(constante, d1))
print("------------------------------------------------------------------------------------")

# Opérandes à plusieurs chiffres.
constante = -50
d1 = 10
print("------------------------------------------------------------------------------------")
print("Test : 5 : Les opérandes sont {} pour la constante et {} pour la variable en X : ".format(constante, d1))
print(resoudreD1(constante, d1))
print("------------------------------------------------------------------------------------")


print("#######################################################################################")
print("Test de la fonction \"resoudreD2(constante, d1, d2)\"")
print("#######################################################################################")

# Opérandes à plusieurs chiffres.
constante = -50
d1 = 10
d2 = 20
print("------------------------------------------------------------------------------------")
print("Test : 1 : Les opérandes sont {} pour la constante, {} pour la variable en X et {} pour la variable en X². : ".format(constante, d1, d2))
resoudreD2(constante, d1, d2)
print("------------------------------------------------------------------------------------")

# Equation sans solution.
constante = 1
d1 = 1
d2 = 2
print("------------------------------------------------------------------------------------")
print("Test : 2 : Les opérandes sont {} pour la constante, {} pour la variable en X et {} pour la variable en X². : ".format(constante, d1, d2))
resoudreD2(constante, d1, d2)
print("------------------------------------------------------------------------------------")


# Equation dont le discriminant vaut 0.
constante = 3
d1 = -6
d2 = 3
print("------------------------------------------------------------------------------------")
print("Test : 3 : Les opérandes sont {} pour la constante, {} pour la variable en X et {} pour la variable en X². : ".format(constante, d1, d2))
resoudreD2(constante, d1, d2)
print("------------------------------------------------------------------------------------")


# Equation classique avec opérandes à un chiffre.
constante = -6
d1 = 1
d2 = 2
print("------------------------------------------------------------------------------------")
print("Test : 4 : Les opérandes sont {} pour la constante, {} pour la variable en X et {} pour la variable en X². : ".format(constante, d1, d2))
resoudreD2(constante, d1, d2)
print("------------------------------------------------------------------------------------")


# Equation dont l'opérande en X vaut 0.
constante = -2
d1 = 0
d2 = 3
print("------------------------------------------------------------------------------------")
print("Test : 5 : Les opérandes sont {} pour la constante, {} pour la variable en X et {} pour la variable en X². : ".format(constante, d1, d2))
resoudreD2(constante, d1, d2)
print("------------------------------------------------------------------------------------")


# Equation dont l'opérande constante vaut 0.
constante = 0
d1 = 0
d2 = 3
print("------------------------------------------------------------------------------------")
print("Test : 6 : Les opérandes sont {} pour la constante, {} pour la variable en X et {} pour la variable en X². : ".format(constante, d1, d2))
resoudreD2(constante, d1, d2)
print("------------------------------------------------------------------------------------")







