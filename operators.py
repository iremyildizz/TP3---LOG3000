"""
Module operators

Fournit les fonctions représentant les opérations arithmétiques de base
utilisées par l'application de calculatrice Flask.
Les fonctions définies ici sont appelées depuis la fonction `calculate` du module `app`.
"""

def add(a,b):

    """
    Calcule la somme de deux nombres.

    :param a: premier opérande
    :param b: deuxième opérande
    :return: somme de a et b
    """
    return a + b

def subtract(a,b):
    """
    Calcule la différence entre deux nombres.

    :param a: premier opérande
    :param b: deuxième opérande
    :return: différence entre b et a
    """
    return b - a

def multiply(a,b):
    """
    Calcule le produit de deux nombres.

    :param a: premier opérande
    :param b: deuxième opérande
    :return: produit de a et b
    """
    return a * b

def divide(a,b):
    """
    Calcule la division de deux nombres.

    :param a: premier opérande
    :param b: deuxième opérande
    :return: résultat de la division de a par b
    """
    return a // b
