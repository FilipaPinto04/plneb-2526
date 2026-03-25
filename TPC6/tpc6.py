import spacy
from spacy.matcher import Matcher
import json
from collections import defaultdict

nlp = spacy.load("pt_core_news_lg") 
f = open("C:\\Users\\Filipa Pino\\Desktop\\Processamento de Linguagem Natural\\Dados\\Harry Potter e A Pedra Filosofal.txt",encoding='utf-8')
texto = f.read()
doc = nlp(texto)

matcher = Matcher(nlp.vocab)
pattern = [{"ENT_TYPE": "PER", "OP": "+"}]
matcher.add("PERSONAGEM", [pattern])

relacoes = defaultdict(lambda: defaultdict(int))

for sent in doc.sents:
    matches = matcher(sent.as_doc())
    
    nomes_na_frase = []
    for match_id, start, end in matches:
        nome = sent[start:end].text.strip()
        
        if nome and len(nome) > 2 and nome[0].isupper():
            if nome not in nomes_na_frase:
                nomes_na_frase.append(nome)
    
    if len(nomes_na_frase) > 1:
        for p1 in nomes_na_frase:
            for p2 in nomes_na_frase:
                if p1 != p2:
                    relacoes[p1][p2] += 1

f = open('friends.json', 'w', encoding='utf-8')
json.dump(relacoes, f, ensure_ascii=False, indent=4)
f.close()