# Calculatrice Web – LOG3000 (TP3)

- **Équipe :** 10
- **Membres :** Pablo Cabale Guerra, Irem Yildiz, Raphael Ramanitranja
- **Cours :** LOG3000 – Processus du génie logiciel

# Description du Projet

    Cette application est une calculatrice web simple développée avec Python (Flask).
    Elle permet d’effectuer les opérations arithmétiques de base — addition, soustraction, multiplication et division — à travers une interface web interactive.

    Le projet a pour but d’illustrer les bonnes pratiques de génie logiciel dans un environnement collaboratif :

        - utilisation de GitHub (issues, branches, pull requests),

        - documentation claire du code et des modules,

        - ajout de tests unitaires et d’un pipeline de vérification,

        - gestion de versions structurée.

    Ce projet a été réalisé dans le cadre du cours LOG3000 – Processus du génie logiciel à Polytechnique Montréal.

## Objectif du projet

    Ce projet est une **application web de calculatrice simple** développée avec **Python (Flask)**.
    L’objectif principal est de :

    - explorer une base de code existante,
    - mettre en place de bonnes pratiques de gestion de versions avec Git/GitHub,
    - documenter le projet,
    - ajouter des tests et corriger les bogues.

# Structure du Projet

        TP3---LOG3000/
        ├── app.py
        ├── operators.py
        ├── templates/
        │ └── index.html
        ├── static/
        │ └── style.css
        ├── tests/
        │ └── test_operators.py
        └── README.md

## Prérequis

Avant d’installer le projet, vous devez avoir :

- **Python** (version 3.10+)
- **pip** (gestionnaire de paquets Python)
- **Git**
- Un compte **GitHub** (pour cloner le dépôt)
- (Optionnel mais recommandé) **Un environnement virtuel (`venv`)**

Vous pouvez vérifier les versions installées avec :

```bash
python --version
pip --version
git --version
```

## Installation

Suivez ces étapes pour exécuter localement l’application :

    1. Cloner le dépôt GitHub
        git clone https://github.com/<TON-UTILISATEUR>/<NOM-DU-REPO>.git
        cd TP3---LOG3000

    2. Créer et activer un environnement virtuel (recommandé)
        python -m venv venv
        source venv/bin/activate       # macOS/Linux
        venv\Scripts\activate          # Windows

    3. Installer les dépendances
        pip install flask pytest

        Si un fichier requirements.txt existe, utilisez :
            pip install -r requirements.txt

    4. Lancer l’application
        python app.py

    Le serveur sera accessible à l’adresse :
        http://127.0.0.1:5000/

## Utilisation de l'application

    1. Ouvrir le navigateur sur http://127.0.0.1:5000/

    2. Saisir une expression simple dans la calculatrice, par exemple :
        - 1+2
        - 5-3
        - 4*2
        - 10/5

    3. Cliquer sur le bouton = pour exécuter le calcul.

    4. En cas d’erreur (ex. division par zéro ou syntaxe invalide), le message d’erreur s’affiche dans l’écran de la calculatrice.

## Tests

    Des tests unitaires ont été ajoutés dans le dossier tests/ afin de valider :
        - le comportement des fonctions dans operators.py,
        - la robustesse de la fonction calculate() de app.py,
        - la gestion des erreurs (ValueError, ZeroDivisionError, etc.).

### Exécuter les tests

    1. ssurez-vous d’être dans le dossier du projet et que Flask n’est pas en cours d’exécution.

    2. Lancer Pytest :
        pytest

    3. Les résultats s’afficheront dans le terminal, par exemple :

        ================== test session starts ==================
        collected 10 items

        tests/test_operators.py ....F... [100%]

        ================== 1 failed, 9 passed in 0.34s ==================

    Les tests échoués correspondent à des bogues qui devront être corrigés dans les branches correspondantes.

## Flux de Contribution

    Afin d'assurer une bonne gestion de git, l'equipe a suivi le flux suivant:

    **Les Branches**
        - main : la branche principale, stable et fonctionnelle
        - feature/ : nouvelles fonctionnalités
        - fix/ : corrections de bogues

    **Processus Standard**
        1. Identifier un bug ou une amélioration et ouvrir une Issue GitHub :
            - titre clair (ex. “Bug : mauvaise soustraction dans operators.py”)
            - description complète (étapes, résultat attendu, résultat obtenu)

        2. Créer une nouvelle branche associée :
            - git checkout -b fix/issue-1-soustraction

        3. Corriger le code et committer avec un message explicite :
            - git add .
            - git commit -m "Fix issue #1: correction de la fonction subtract()"

        4. Pousser la branche et ouvrir une Pull Request sur GitHub :
            - git push origin fix/issue-1-soustraction

        5. Faire une revue de code (peer review) avant la fusion.

        6. Fusionner la PR sur main une fois les tests passés.

## Notes Techniques

    - Le serveur Flask utilise le module operators.py pour effectuer les calculs.

    - L’interface HTML est gérée dans templates/index.html avec du JavaScript minimal (aucun framework JS).

    - Les styles sont définis dans static/style.css (aucun framework CSS externe).

    - L’application ne gère actuellement qu’une seule opération à la fois (ex. 2+3), sans priorité ni parenthèses.

## Auteurs

    Projet développé par l’équipe #10 dans le cadre du cours LOG3000 – Processus du génie logiciel Polytechnique Montréal, Automne 2025.

    **Membres de l'équipe:**
    - Pablo Cabale Guerra
    - Irem Yildiz
    - Raphael Ramanitranja
