import spacy
import math

nlp = spacy.load("en_core_web_sm")

collection = ["The sky is blue",
              "The sun is bright",
              "The sun in the sky"]

#remover stop words, tirar pontuacao e por tudo letras minuscula, tokenizar
def pre_processamento(collection):
    new_collection = []
    for doc_text in collection:
        s_doc = nlp(doc_text)
        tokens_limpos = [
            token.lower_ 
            for token in s_doc 
            if not token.is_stop and not token.is_punct and not token.is_space
        ]
        new_collection.append(tokens_limpos)
    return new_collection

#tf(t,d) = count(t)/total words(d)
def tf(doc):
    N = len(doc)
    res = {}
    for term in doc:
        if term in res:
            res[term] += 1
        else:
            res[term] = 1

    res = {k: v/N for k,v in res.items()}
    return res #{"termo": freq}

#idf(t,D) = log(N,df)
def idf(collection):
    N = len(collection)
    res = {}
    unique_terms = set([term for d in collection for term in d])
    for term in unique_terms:
        counter = 0
        for doc in collection:
            if term in doc:
                counter += 1
        rarity = math.log(N/counter,10)
        res[term] = rarity
    return res #{termo: rarity}

# tf_idf(t,d,D) = tf(t,d) * idf(t,D)
def tf_idf(collection):
    res = []
    idf_values = idf(collection)
    vocabulary = sorted(list(idf_values.keys()))
    for doc in collection:
        doc_tf_idf = []
        tf_values = tf(doc)
        for term in vocabulary:
            if term in tf_values:
                # TF-IDF(t, d) = TF(t, d) * IDF(t, D) [cite: 93, 164]
                valor = tf_values[term] * idf_values[term]
                doc_tf_idf.append(valor)
            else:
                # Se o termo do vocabulário não está no doc, o peso é 0
                doc_tf_idf.append(0.0)
        res.append(doc_tf_idf)
    return res, idf_values, vocabulary

def cosine_similarity(v1, v2):
    dot_product = 0
    sum_sq_v1 = 0
    sum_sq_v2 = 0
    
    for i in range(len(v1)):
        dot_product += v1[i] * v2[i]
        sum_sq_v1 += v1[i] ** 2      
        sum_sq_v2 += v2[i] ** 2      
    
    mag1 = math.sqrt(sum_sq_v1)
    mag2 = math.sqrt(sum_sq_v2)
    
    if not mag1 or not mag2:
        return 0.0
        
    return dot_product / (mag1 * mag2)


docs_tokens = pre_processamento(collection)
doc_vectors, corpus_idf, vocabulary = tf_idf(docs_tokens)


query_text = "The bright sun"
query_tokens = pre_processamento([query_text])[0] 

# Vetorizar a Query
query_tf = tf(query_tokens)
query_vector = []
for term in vocabulary:
    if term in query_tf:
        # Peso = TF(query) * IDF(corpus)
        query_vector.append(query_tf[term] * corpus_idf[term])
    else:
        query_vector.append(0.0)

print(f"Vetor da Query: {query_vector}\n")

melhor_doc_idx = -1
maior_sim = -1

for i, doc_vec in enumerate(doc_vectors):
    sim = cosine_similarity(query_vector, doc_vec)
    print(f"Similaridade com D{i+1} ('{collection[i]}'): {sim:.4f}")
    
    if sim > maior_sim:
        maior_sim = sim
        melhor_doc_idx = i

print(f"\nO documento mais relevante é o D{melhor_doc_idx + 1}: '{collection[melhor_doc_idx]}'")