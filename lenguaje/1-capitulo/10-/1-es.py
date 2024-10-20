import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Añade el patrón al matcher
pattern = [{"TEXT": "adidas"}, {"TEXT": "zx"}]
matcher.add("ADIDAS_PATTERN", [pattern])

# Procesa un texto
doc = nlp("Nuevos diseños de zapatillas en la colección adidas zx")

# Llama al matcher sobre el doc
matches = matcher(doc)

print(doc)
print(matches)
