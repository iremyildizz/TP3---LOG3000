"""
Module de tests pour l'application de calculatrice.


Ce module contient des tests unitaires pour :
- les fonctions d'opérations arithmétiques définies dans operators.py ;
- la fonction calculate définie dans app.py.

Les tests vérifient le comportement attendu de la calculatrice.
Certains tests sont volontairement écrits pour révéler des bogues
dans l'implémentation actuelle (par exemple la soustraction ou la division).
"""
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

import pytest
from operators import add, subtract, multiply, divide
from app import calculate

def test_addition_two_positive_numbers():
    """
    Vérifie que add retourne bien la somme de deux nombres positifs.
    """
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(-1, 1) == 0

def test_subtraction_two_positive_numbers():
    """
    Vérifie que subtract retourne bien a - b.

    Ce test devrait échouer tant que la fonction subtract
    ne respecte pas la spécification (a - b).
    """
    assert subtract(5, 3) == 2   # attendu : 5 - 3 = 2
    assert subtract(3, 5) == -2  # attendu : 3 - 5 = -2

def test_multiply_two_simple_numbers():
    """
    Vérifie que multiply retourne le produit de deux nombres.
    """
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0


def test_division_returns_a_float():
    """
    Vérifie que divide effectue une division "normale" (a / b)
    et non une division entière.

    Ce test devrait échouer tant que divide utilise l'opérateur //.
    """
    assert divide(4, 2) == 2.0
    assert divide(7, 2) == 3.5  # division flottante attendue


def test_division_by_zero_raises_exception():
    """
    Vérifie que la division par zéro lève bien une exception.
    """
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


# ---------- Tests pour app.calculate ----------

def test_calculate_simple_addition():
    """
    Vérifie que calculate évalue correctement une addition simple.
    """
    result = calculate("2+3")
    assert result == 5.0


def test_calculate_multiplication_with_spaces():
    """
    Vérifie que calculate gère les espaces dans l'expression.
    """
    result = calculate(" 3 * 4 ")
    assert result == 12.0


def test_calculate_floating_division():
    """
    Vérifie que calculate retourne un flottant pour une division.

    Ce test révélera aussi le problème si divide utilise //.
    """
    result = calculate("7/2")
    assert result == 3.5


def test_calculate_empty_expression_raises_valueerror():
    """
    Vérifie qu'une expression vide provoque une ValueError.
    """
    with pytest.raises(ValueError):
        calculate("")


def test_calculate_multiple_operators_raises_valueerror():
    """
    Vérifie qu'une expression avec plusieurs opérateurs (ex: 1+2-3)
    provoque une ValueError comme prévu.
    """
    with pytest.raises(ValueError):
        calculate("1+2-3")


def test_calculate_non_numeric_operands_raises_valueerror():
    """
    Vérifie qu'une expression avec des opérandes non numériques
    provoque une ValueError.
    """
    with pytest.raises(ValueError):
        calculate("a+2")


def test_calculate_division_by_zero_propagates_zero_division_error():
    """
    Vérifie que calculate propage l'erreur de division par zéro.

    L'appel à divide(4, 0) devrait lever ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        calculate("4/0")
