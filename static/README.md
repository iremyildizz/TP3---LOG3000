# static

Ce répertoire contient les fichiers statiques utilisés par l'application.

## Fichiers

- `style.css` : feuille de style principale pour la calculatrice.
  - Définit la mise en page, les couleurs, la disposition des boutons, etc.

## Dépendances / hypothèses

- Le fichier est servi par Flask comme fichier statique et inclus dans `templates/index.html`.
- Aucun outil externe (Sass, Less, etc.) n'est utilisé, le CSS est écrit directement.
