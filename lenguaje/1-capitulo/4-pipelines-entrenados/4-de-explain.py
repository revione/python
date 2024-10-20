import spacy

# Lade die kleine deutsche Pipeline
nlp = spacy.load("de_core_news_sm")

oa = spacy.explain("oa")

nnp = spacy.explain("NNP")

misc = spacy.explain("MISC")


print("oa = ", oa)
print("NNP = ", nnp)
print("MISC = ", misc)