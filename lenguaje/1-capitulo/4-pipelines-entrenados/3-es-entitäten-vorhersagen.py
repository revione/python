import spacy

# Lade die kleine deutsche Pipeline
nlp = spacy.load("de_core_news_sm")

# Verarbeite einen Text
doc = nlp("Apple stellt in Cupertino das neue iPhone vor")

# Iteriere über die vorhergesagten Entitäten
for ent in doc.ents:
    # Drucke den Text und das Label der Entität
    print(ent.text, ent.label_)