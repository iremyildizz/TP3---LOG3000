# templates

Ce répertoire contient les templates HTML utilisés par l'application Flask.

## Fichier principal

- `index.html` : page principale de la calculatrice.
  - Affiche le champ d'affichage (`display`).
  - Contient les boutons numériques et d'opérations.
  - Soumet l'expression complète au serveur lorsque l'utilisateur clique sur "=".

## Dépendances / hypothèses

- Les templates sont rendus par la fonction `index` du module `app.py` via `render_template`.
- Les styles sont fournis par le fichier `static/style.css`.
