from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

with open("dicionario_medico.json", "r", encoding="utf-8") as f_db:
    db = json.load(f_db)


def find_concept(query):
    query_lower = query.lower()
    for chave in db.keys():
        if chave.lower() == query_lower:
            return chave
    return None


@app.get("/")
def home_page():
    primeiros_conceitos = random.sample(list(db.keys()), 6)
    return render_template("home.html", conceitos=primeiros_conceitos)


@app.get("/api/conceitos")
def conceitos_api():
    return db


@app.get("/conceitos")
def listar_conceitos():
    query = request.args.get("q", "").strip()
    if query:
        chave = find_concept(query)
        if chave:
            return render_template("conceito.html", designacao=chave, descricao=db[chave])
        return render_template("error.html", erro=f"O conceito '{query}' não existe no dicionário."), 404
    return render_template("conceitos.html", conceitos=db.keys())


@app.get("/conceitos/<designacao>")
def conceito(designacao):
    chave = find_concept(designacao)
    if chave:
        return render_template("conceito.html", designacao=chave, descricao=db[chave])
    return render_template("error.html", erro=f"O conceito '{designacao}' não existe."), 404


if __name__ == "__main__":
    app.run(host="localhost", port=4002, debug=True)
