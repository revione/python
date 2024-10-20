import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

doc = nlp("A mi me gusta mucho comer pizza")

for token in doc:
    print(token.text, spacy.explain(token.pos_), spacy.explain(token.dep_), token.head.text)