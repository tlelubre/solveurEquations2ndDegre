"""
Module comportant un ensemble de fonctions pour résoudre des équations.
Créé initialement pour le module "resolveurEquationsSimples".

"""

import math # Module contenant des outils mathématiques.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def determinerOperandes(equation):
    """
    Récupère les différentes opérandes composant une équation. (fonctionne jusqu'aux équation de degré > 9)

    Paramètre
    ---------

    ->equation : L'équation dont il faut extraire les opérandes. (str)
                 Cette équation doit correspondre aux normes spécifiées dans le module "resolveurEquationsSimple".

    Retour
    ------

    ->operandes : Une liste contenant les opérantes de l'équation. Chaque élément de la liste est une opérande distincte de l'équation. (list)

    """

    index = 0
    operande = ""
    operandes = []

    while (index < len(equation)): # Parcours de l'équation.

        if (equation[index] == "-"): # Gérer les opérandes négatives.
            if (len(operande) > 0): # Si la condition est vraie, alors cela signifie que l'on passe à une autre opérande, qui est négative.
                operandes.append(operande)
                operande = ""
            operande += "-"


        while (index < len(equation)) and ((equation[index].isdigit()) or equation[index] == "."): # Gérer les nombres. (mêmes ceux à virgule)
            operande += equation[index]
            index += 1

        if (index < len(equation)) and (equation[index] == "X"): # Gérer les variables "X". Déterminer le degré d'une opérande, et la capturer.
            operande += "X"
            if (index + 1 < len(equation)) and (equation[index+1] == "^"):
                operande += "^"+equation[index+2] # Permet de capturer les opérandes jusqu'au degré 9.
                index += 3
        
        if (index >= len(equation)) or (equation[index] == "+"): # Gérer le passage à une autre opérande quand elle est positive.
            operandes.append(operande)
            operande = ""

        index += 1
    
    if (operande): # Ne pas oublier d'ajouter la dernière opérande.
        operandes.append(operande)

    return operandes

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def trierOperandes(operandes):
    """
    Permet de trier les opérandes selon leur degré. (fonctionne pour au maximum le degré 2.)

    Paramètre
    ---------

    ->operandes : La liste contenant toutes les opérandes d'une équation. (list)

    Retours
    -------

    ->listeConstantes : Une liste contenant les opérandes qui sont des constantes. (list)
    ->listeD1 : Une liste contenant les opérandes qui sont de degré 1. (list)
    ->listeD2 : Une liste contenant les opérandes qui sont de degré 2. (list)


    """
    listeConstantes = []
    listeD1 = []
    listeD2 = []

    # Parcours des différentes liste.
    for operande in operandes:
        if "X^2" in operande: # Ajout d'une opérande de dégré 2 à sa liste.
            listeD2.append(operande)
        elif "X" in operande: # Ajout d'une opérande de dégré 1 à sa liste.
            listeD1.append(operande)
        else: # Ajout d'une opérande constante à sa liste.
          listeConstantes.append(operande)
    
    return listeConstantes, listeD1, listeD2

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def extrairePartieEntiere(operandesD2, operandesD1, operandesConst):
    """
    Additionne les opérandes de degré équivalent.

    Paramètres
    ----------

    ->operandesD2 : Une liste d'opérandes de degré 2. (list)
    ->operandesD1 : Une liste d'opérandes de degré 1. (list)
    ->operandesConst : Une liste d'opérandes qui sont des constantes. (list)

    Retours
    -------

    ->resultConst : Le résultat de l'addition des différentes opérandes constantes données par le paramètre operandesConst. (float)
    ->resultD1 : Le résultat de l'addition des différentes opérandes de degré 1 données par le paramètre operandesD1. (float)
    ->resultD2 : Le résultat de l'addition des différentes opérandes de degré 2 données par le paramètre operandesD2. (float)

    """

    resultD2 = 0
    resultD1 = 0
    resultConst = 0

    for d2 in operandesD2:
        if (not(d2[:d2.find("^")-1])): # Vérifier si la partie constante de la variable x² est 1.
            resultD2 += 1 
        else:
            resultD2 += float(d2[:d2.find("^")-1]) # Récupérer la partie constante de la variable X².

    for d1 in operandesD1:
        if (not(d1[:d1.find("X")])): # Vérifier si la partie constante de la variable x est 1.
            resultD1 += 1
        else:
            resultD1 += float(d1[:d1.find("X")]) # Récupérer la partie constante de la variable X.

    for const in operandesConst:
        resultConst += float(const) # Récupérer la constante résultante.

    return resultConst, resultD1, resultD2

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def resoudreD1(constante, d1):
    """
    Résout une équation simplifiée de degré 1.

    Paramètres
    ----------

    ->constante : La valeur de la constante de l'équation simplifiée. (float)
    ->d1 : La valeur réelle constituant l'opérande en X. (float)

    Retour
    ------

    ->solution : La solution de l'équation simplifiée de degré 1. (float)

    """

    solution = (-1 * constante) / d1
    print("Le résultat de l'équation est :", solution)
    return solution

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def resoudreD2(constante, d1, d2):
    """
    Résout une équation simplifiée de degré 2.

    Paramètres
    ----------

    ->constante : La valeur de la constante de l'équation simplifiée. (float)
    ->d1 : La valeur réelle constituant l'opérande en X. (float)
    ->d2 : La valeur réelle constituant l'opérande en X². (float)

    """
    discriminant = (d1**2) - (4*d2*constante)
    if (discriminant < 0):
        print("L\'équation n'a pas de solution.")
    elif (discriminant == 0):
        solution = (-1*d1) / (2*d2)
        print("La solution de l\'équation est : ", solution)
    else:
        solution1 = ((-1*d1) + math.sqrt(discriminant)) / (2*d2)
        solution2 = ((-1*d1) - math.sqrt(discriminant)) / (2*d2)
        print("Les solutions de l\'équation sont :", solution1, "et ", solution2)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------