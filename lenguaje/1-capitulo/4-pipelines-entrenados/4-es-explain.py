import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

spacy.explain("LOC")

spacy.explain("NNP")

spacy.explain("MISC")