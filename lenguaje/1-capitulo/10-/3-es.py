import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido




# 1
matcher1 = Matcher(nlp.vocab)
pattern1 = [
    {"IS_DIGIT": True},
    {"LOWER": "copa"},
    {"LOWER": "mundial"},
    {"LOWER": "fifa"},
    {"IS_PUNCT": True}
]
matcher1.add("MUNDIAL_PATTERN", [pattern1])
doc1 = nlp("2014 Copa Mundial FIFA: Alemania ganó!")
matches1 = matcher1(doc1)

for match_id, start, end in matches1:
    # Obtén el span resultante
    matched_span = doc1[start:end]
    print(matched_span.text)



# 2
matcher2 = Matcher(nlp.vocab)
pattern2 = [
    {"LEMMA": "comer", "POS": "VERB"},
    {"POS": "NOUN"}
]
matcher2.add("COMER_PATTERN", [pattern2])
doc2 = nlp("Camila prefería comer sushi. Pero ahora está comiendo pasta.")
matches2 = matcher2(doc2)


for match_id, start, end in matches2:
    # Obtén el span resultante
    matched_span = doc2[start:end]
    print(matched_span.text)


# 2
matcher3 = Matcher(nlp.vocab)
pattern3 = [
    {"LEMMA": "comprar"},
    {"POS": "DET", "OP": "?"},  # opcional: encuentra 0 o 1 ocurrencias
    {"POS": "NOUN"}
]
matcher3.add("COMPRAR_PATTERN", [pattern3])
doc3 = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")
matches3 = matcher3(doc3)


for match_id, start, end in matches3:
    # Obtén el span resultante
    matched_span = doc3[start:end]
    print(matched_span.text)


# # Ejemplo     # Descripción
# {"OP": "!"}   Negación: busca O veces
# {"OP": "?"}   Opcional: busca 0 o 1 veces
# {"ОР": "+"}   Busca 1 o más veces
# {"ОР": "*"}   Busca O o más veces