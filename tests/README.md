# Module de tests – TP3 LOG3000

## Objectif

Ce dossier contient les tests automatisés pour l’application **Calculatrice Web (Flask)**.  
Les tests servent à valider à la fois les opérations arithmétiques du module operators.py et le comportement global de la fonction calculate dans app.py.

Les tests ont été conçus à l’aide du framework pytest, afin de faciliter l’exécution et la validation continue du code.

## Contenu

- **test_calculator.py** :
  Contient les tests unitaires pour les fonctions arithmétiques de base :

add(a, b)

subtract(a, b)

multiply(a, b)

divide(a, b)

- **test_app_calculate.py** :
  Contient les tests unitaires pour la fonction calculate(expr) du module app.py.
  Ces tests vérifient :

l’évaluation correcte d’expressions simples (ex. "2+3", "3\*4") ;

la gestion des espaces et des erreurs (ValueError, ZeroDivisionError) ;

le comportement attendu lors de divisions et soustractions incorrectes.

Chaque fonction de test inclut :

- une docstring décrivant son rôle ;
- des assertions claires pour comparer le résultat obtenu au résultat attendu.

## Prérequis

Avant d’exécuter les tests, assurez-vous d’avoir installé :

- Python 3.10 ou plus récent
- le paquet `pytest` :

```bash
pip install pytest
```

## Éxécution des tests

Depuis la racine du projet, exécuter :

- pytest -v

Pour lancer uniquement un fichier de tests spécifique :

- pytest -v tests/test_operators.py
- pytest -v tests/test_app_calculate.py
