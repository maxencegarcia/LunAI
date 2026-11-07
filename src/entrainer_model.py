from intent_classifier import IntentClassifier
from dataloader import chargerexemple

textes, etiquettes = chargerexemple()

model = IntentClassifier()
model.train(textes, etiquettes)
# verif
print(model.predire("bonjour"))
model.save("Lunav1")