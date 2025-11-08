"""
Module app

Définit l'application Flask de la calculatrice web. Ce module contient :
- la configuration de l'application Flask ;
- le dictionnaire d'opérateurs `OPS` reliant les symboles (+, -, *, /) aux fonctions
  définies dans `operators.py` ;
- la fonction `calculate` qui interprète et évalue une expression arithmétique simple ;
- la route principale `/` qui affiche l'interface HTML et renvoie le résultat à l'utilisateur.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):

    """
    Évalue une expression arithmétique simple de la forme « a op b ».

    L'expression doit contenir exactement deux opérandes numériques (entiers ou flottants)
    et un seul opérateur parmi ceux définis dans le dictionnaire OPS :
    - "+"
    - "-"
    - "*"
    - "/"

    Les espaces dans l'expression sont ignorés. Quelques exemples :

    Exemples d'expressions valides :
    - "1+2"
    - " 3.5 * 4 "
    - "10/2"

    Exemples d'expressions invalides :
    - "" (expression vide)
    - "1++2" (plusieurs opérateurs)
    - "+2" ou "2+" (opérateur au début ou à la fin)
    - "a+2" (opérandes non numériques)

    :param expr: expression arithmétique à analyser et évaluer.
    :raises ValueError: si l'expression est vide, mal formée ou si les opérandes
                        ne peuvent pas être converties en nombres.
    :return: le résultat numérique (float) de l'opération demandée.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application de calculatrice.

    - En méthode GET :
      * renvoie la page HTML de la calculatrice avec un affichage initial vide.

    - En méthode POST :
      * récupère l'expression saisie par l'utilisateur dans le champ "display" ;
      * appelle la fonction `calculate` pour évaluer l'expression ;
      * en cas de succès, affiche le résultat ;
      * en cas d'erreur (expression invalide, division par zéro, etc.), affiche un message
        d'erreur textuel retourné sous la forme "Error: <message>".

    :return: le template `index.html` rendu avec la variable de contexte `result`.
    """
    
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)