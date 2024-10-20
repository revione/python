import spacy

# Cargar el modelo de procesamiento del alemán
nlp = spacy.load("de_core_news_md")

# Oración de ejemplo
# doc = nlp("Eigentlich kann er nicht gut schwimmen.")
# doc = nlp("Ah, du hast recht. Wir sollten die Natur genißen.")
# doc = nlp("Ich habe meinem Freund ein Geschenk gegeben.")
doc = nlp(
"Dieses Quartal ist wichtig."
"Deine Schwester ist dir ähnlich."
"Die einfachen Bücher gefallen ihm."
"Du bist eine Maus ähnlich."
"Eingentlich kann er nicht gut schwimmen."
"Er hat ein Telefon."
"Das Quartal beginnt in September."
"Vater wo ist unser Mitwagen?"
"Die Medizin wird wirken."
"Wo ist dein Telefon?"
"Die Medizin wird wirken."
"Einen Mietwagen, bitte."
"Mir geht es eigentlich gut."
"Das Quartal beginnt im September."
)

# print(nlp.meta["sources"])

# Iterar sobre cada token en la oración
for token in doc:
    # print(token.text, spacy.explain(token.pos_), spacy.explain(token.dep_), token.head.text, token.tag_, token.morph)
    print(token.text, spacy.explain(token.pos_), token.tag_, token.morph)
    # print(f"{token.text:>10}{spacy.explain(token.pos_):>10}{token.morph:>10}")
