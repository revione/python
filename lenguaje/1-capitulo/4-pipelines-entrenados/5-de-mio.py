import spacy

# Lade die kleine deutsche Pipeline
nlp = spacy.load("de_core_news_sm")

doc = nlp("Eingentlich kann er nicht gut schwimmen.")

for token in doc:
    print(token.text, spacy.explain(token.pos_), spacy.explain(token.dep_), token.head.text)