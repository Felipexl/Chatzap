# cdnjs.com - para ver bibliotecas HTML

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# enviar mensagens
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a primeira página
@app.route("/")
def homepage():
    return render_template ("index.html")

# roda o aplicativo
socketio.run(app, host="192.168.0.243")
