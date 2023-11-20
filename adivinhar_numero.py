
from flask import Flask, render_template, request
# Questão 1, primeiro item
import random

app = Flask(__name__)

# Questao 1, segundo item
# numero_secreto = 
import random

numero_secreto = random.randint(1, 100)


@app.route("/", methods=['GET', 'POST'])
def checar_palpite():
    mensagem = ''
    if request.method == 'POST':
        palpite = request.form['palpite']
        # Questão 2, primeiro item
        print(type(palpite))
        palpite_1 = int(palpite)

        # Questão 2, segundo item
        if palpite_1 > numero_secreto: 
            mensagem = "Tente um número menor"
        elif palpite_1 < numero_secreto:
            mensagem = "Tente um número maior"
        else: 
            mensagem = f"parabéns!! você acertou o número {numero_secreto} "

    return render_template('adivinhar_numero.html', mensagem=mensagem)