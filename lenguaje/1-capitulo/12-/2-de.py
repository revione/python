import spacy

# Importiere den Matcher
from spacy.matcher import Matcher

# Lade ein Modell und erstelle das nlp-Objekt
nlp = spacy.load("de_core_news_sm")

# Initialisiere den Matcher mit dem gemeinsamen Vokabular
matcher = Matcher(nlp.vocab)

# Füge das Pattern zum Matcher hinzu
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Verarbeite einen Text
doc = nlp("Das neue iPhone X erscheint demnächst in Deutschland")

# Rufe den Matcher mit dem Doc auf
matches = matcher(doc)

print(matches)