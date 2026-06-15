from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jogo/cobrinha')
def jogo_cobrinha():
    return render_template('cobrinha.html')

# @app.route('/jogo/velha')
# def jogo_velha():
#     return render_template('velha.html')

@app.route('/jogo/memoria')
def jogo_memoria():
    return render_template('memoria.html')

@app.route('/jogo/invaders')
def jogo_invaders():
    return render_template('invaders.html')

@app.route('/jogo/breakout')
def jogo_breakout():
    # Nova rota para o Jogo do Paredão Breakout
    return render_template('breakout.html')

if __name__ == '__main__':
    app.run(debug=True)
