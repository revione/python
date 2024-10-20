import spacy

nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp(
    "Apple es la marca que más satisfacción genera en EE.UU., "
    "pero el iPhone, fue superado por el Galaxy Note 9"
)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto y la etiqueta de la entidad
    print(ent.text, ent.label_)