from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogo4 = Jogo('Need for Speed', 'Corrida', 'PS2')
jogo5 = Jogo('Valorant', 'FPS', 'PC')
lista = [jogo1, jogo2, jogo3, jogo4, jogo5]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario = Usuario("Matheus Martins", "MM",  "Palmeiras")
usuario2 = Usuario("Maria Eduarda", "ME", "Palmeiras@1009")
usuario3 = Usuario("Caio Lacerda", "CL", "0909")

usuarios = {usuario.nickname : usuario,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3}

app = Flask(__name__)
app.secret_key = 'batman'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.arts.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso!')
            proxima_pag = request.form['prox']
            return redirect(proxima_pag)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/sair')
def logout():
    session['usuario_logado'] = None
    flash('Logout feito!')
    return redirect(url_for('index'))

app.run(debug=True)
