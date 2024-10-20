import spacy

# Lade die kleine deutsche Pipeline
nlp = spacy.load("de_core_news_sm")

# Verarbeite einen Text
doc = nlp("Sie aß die Pizza")
# doc = nlp("Eingentlich kann er nicht gut schwimmen.")

# Iteriere über die Tokens
for token in doc:
    # Drucke den Text und die vorhergesagte Wortart
    print(token.text, token.pos_)

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)