from flask import Flask , send_file
from download import coletar_dados
from tratamento import tratar_dados

app = Flask(__name__)


@app.route("/")
def hello_world():
    coletar_dados()
    tratar_dados()
    return send_file('dados_sefaz_ac_soma.csv', as_attachment=True)
