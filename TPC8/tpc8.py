from flask import Flask, render_template, request
import json
import re


app = Flask(__name__)

f_db = open("dicionario_medico.json", "r", encoding="utf-8")
db = json.load(f_db)


@app.get("/")
def home_page():
    return render_template("home.html")

@app.get("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos=db.keys())

@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template("conceito.html", designacao=designacao, descricao=descricao)
    else:
        return render_template("erro.html", erro="O conceito introduzido não existe")

@app.get("/api/conceitos")
def conceitos_api():
    return db

@app.post("/conceitos")
def adicionar_conceitos():
    descricao = request.form["descricao"]
    designacao = request.form["designacao"]
    db[designacao] = descricao
    f_out = open("bd.json", "w")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return render_template("conceitos.html", conceitos=db.keys())

@app.delete("/conceitos/<designacao>")
def apagar_conceito(designacao):
    del db[designacao]
    f_out = open("bd.json", "w")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return {"redirect_url": "/conceitos", "message": "Conceito apagado com sucesso"}

@app.get("/tabela")
def tabela():
    return render_template("tabela.html", conceitos=db)

@app.get("/pesquisar")
def pesquisar():
    query = request.args.get("q", "")
    exact = request.args.get("exact", "false").lower() == "true"
    case_sensitive = request.args.get("case", "false").lower() == "true"

    resultados = {}

    if query:
        for designacao, descricao in db.items():
            d = designacao if case_sensitive else designacao.lower()
            desc = descricao if case_sensitive else descricao.lower()
            q = query if case_sensitive else query.lower()

            if exact:
                pattern = r'\b' + re.escape(q) + r'\b'
                flags = 0 if case_sensitive else re.IGNORECASE
                match_designacao = re.search(pattern, designacao, flags)
                match_descricao = re.search(pattern, descricao, flags)
                if match_designacao or match_descricao:
                    resultados[designacao] = descricao
            else:
                if q in d or q in desc:
                    resultados[designacao] = descricao

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return resultados

    return render_template("pesquisar.html", query=query)


app.run(host="localhost", port=4002, debug=True)