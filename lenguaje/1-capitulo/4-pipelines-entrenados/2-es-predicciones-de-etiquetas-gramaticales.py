import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp("Ella comió pizza")

# Itera sobre los tokens
for token in doc:
    # Imprime en pantalla el texto y la etiqueta gramatical predicha
    print(token.text, token.pos_)

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)