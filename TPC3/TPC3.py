import re

f = open('dicionario_medico.txt', 'r', encoding='utf8')
text = f.read()

text = re.sub(r'\n\n', '\n\n@', text)
text = re.sub(r'\f', '\n', text)
text = re.sub(r'\n\n@\n([A-ZÀ-Ú])', r'\n\1', text) 
text = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])', r'\1 \2', text)
text = re.sub(r'@', '', text)

blocos = text.split("\n\n")
conceitos_dict = {}

for b in blocos:
    partes = b.strip().split('\n', 1) 
    if len(partes) == 2:
        conceito = partes[0].strip()
        descricao = partes[1].strip()
        conceitos_dict[conceito] = descricao
    elif len(partes) == 1:
        continue

def gera_html(filename, conceitos_dict):
    html="""
<html>
    <head>
        <title> Dicionário Médico </title>
    </head>
    <body> """

    for c in conceitos_dict:
        html = html + f"""
        <div>
        <p> <b>{c} </b> </p>  
        <p> {conceitos_dict[c]} </p>
        </div>
        <hr>
"""

    html = html + """</body>
</html> """

    f_out = open(filename, 'w', encoding='utf8')
    f_out.write(html)
    f_out.close()

gera_html("dicionario_medico.html", conceitos_dict)
print(len(blocos))