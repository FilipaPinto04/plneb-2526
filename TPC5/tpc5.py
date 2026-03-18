from bs4 import BeautifulSoup
import requests
import json
import string

url = f"https://www.atlasdasaude.pt/doencasAaZ/"

def extrair_pagina(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    div_doencas = soup.find_all("div", class_="views-row")

    res = {}
    for div in div_doencas:
        designacao = div.div.h3.a.text 
        
        s_descricao = div.find("div", class_="views-field views-field-body").div.text 

        url_f_desc = div.find("div", class_="views-field views-field-title").a["href"]

        html = requests.get("https://www.atlasdasaude.pt/"+url_f_desc).text
        soup = BeautifulSoup(html, "html.parser")

        full_desc = soup.find("div", class_="field field-name-body field-type-text-with-summary field-label-hidden").div.div.text
            
        res[designacao] = {"Descrição_Resumida": s_descricao.strip(), "Descrição_Completa": full_desc.strip()}

    return res

inf = {}
abc = string.ascii_lowercase
for letra in abc:
    inf = inf | extrair_pagina(url+letra) 

f_out = open("doencasCompleto.json", "w", encoding="utf8")
json.dump(inf, f_out, indent=4, ensure_ascii=False)
f_out.close()