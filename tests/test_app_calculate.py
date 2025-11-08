"""
Tests unitaires pour la fonction calculate du module app.

Ce fichier vérifie :
- l'évaluation correcte d'expressions simples (addition, multiplication, division) ;
- la gestion des espaces dans l'expression ;
- la gestion des erreurs (expression vide, opérateurs multiples, opérandes non numériques,
  division par zéro).
"""

import os
import sys

# Ajouter la racine du projet (TP3---LOG3000) au chemin de recherche des modules
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

import pytest
from app import calculate


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
    Vérifie que calculate retourne le bon résultat pour une division flottante.

    Ce test met en évidence le problème si la fonction divide utilise une division entière.
    """
    result = calculate("7/2")
    assert result == 3.5


def test_calculate_subtraction_expression():
    """
    Vérifie que calculate évalue correctement une soustraction simple.
    """
    result = calculate("5-3")
    assert result == 2.0


def test_calculate_empty_expression_raises_valueerror():
    """
    Vérifie qu'une expression vide provoque une ValueError.
    """
    with pytest.raises(ValueError):
        calculate("")


def test_calculate_multiple_operators_raises_valueerror():
    """
    Vérifie qu'une expression contenant plusieurs opérateurs provoque une ValueError.
    """
    with pytest.raises(ValueError):
        calculate("1+2-3")


def test_calculate_non_numeric_operands_raises_valueerror():
    """
    Vérifie qu'une expression avec des opérandes non numériques provoque une ValueError.
    """
    with pytest.raises(ValueError):
        calculate("a+2")


def test_calculate_division_by_zero_propagates_zero_division_error():
    """
    Vérifie que calculate propage l'erreur de division par zéro
    levée par la fonction divide.
    """
    with pytest.raises(ZeroDivisionError):
        calculate("4/0")
