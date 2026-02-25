def moyenne(tableau):
    """
    Calcule et retourne la moyenne des éléments d'un tableau.

    :param tableau: liste de nombres
    :return: moyenne des valeurs
    """
    somme = 0

    for valeur in tableau:
        somme += valeur

    return somme / len(tableau)


def minimum(tableau):
    """
    Retourne la plus petite valeur du tableau.

    :param tableau: liste de nombres
    :return: valeur minimale
    """
    min_val = tableau[0]

    for valeur in tableau:
        if valeur < min_val:
            min_val = valeur

    return min_val


def maximum(tableau):
    """
    Retourne la plus grande valeur du tableau.

    :param tableau: liste de nombres
    :return: valeur maximale
    """
    max_val = tableau[0]

    for valeur in tableau:
        if valeur > max_val:
            max_val = valeur


    return max_val
