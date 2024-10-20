import spacy

nlp = spacy.load("es_core_news_sm")

text = (
    "Die Olympischen Spiele von Tokio 2020 sind die Inspiration für die neue "
    "Kollektion von Adidas ZX-Sneakers."
)

# Procesa el texto
doc = nlp(text)


# Itera sobre las entidades
for ent in doc.ents:
    # Imprime en pantalla el texto de la entidad y su etiqueta
    print(f"{ent.text:<12}{ent.label_:<10}{spacy.explain(ent.label_):<10}")

# Obtén el span para "adidas zx"
adidas_zx = doc[14:16]

# Imprime en pantalla el texto del span
print("Entidad faltante:", adidas_zx.text,)
