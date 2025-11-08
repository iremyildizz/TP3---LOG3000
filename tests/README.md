# Module de tests – TP3 LOG3000

## 🧩 Objectif

Ce dossier contient les tests automatisés pour l’application **Calculatrice Web (Flask)**.  
Les tests servent à valider les opérations arithmétiques et le comportement général de la fonction `calculate`.

## 📁 Contenu

- **test_calculator.py** : contient tous les tests unitaires pour :
  - les fonctions d’opérations (`add`, `subtract`, `multiply`, `divide`) du module `operators.py` ;
  - la fonction `calculate` du module `app.py`.

Chaque fonction de test inclut :

- une docstring décrivant son rôle ;
- des assertions claires pour comparer le résultat obtenu au résultat attendu.

## ⚙️ Prérequis

Avant d’exécuter les tests, assurez-vous d’avoir installé :

- Python 3.10 ou plus récent
- le paquet `pytest` :

```bash
pip install pytest
```
