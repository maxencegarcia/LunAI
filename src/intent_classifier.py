from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import StratifiedKFold
from dataloader import chargerexemple
textes, etiquettes = chargerexemple()
textes_test, etiquettes_test = chargerexemple("mixintention")


seuilmax = 0.20 # extrait des tests precedant pas complemtement random comme proba 

pipe = Pipeline([
    ("vecteuri", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,5))),
    ("classi", LogisticRegression(C=10, class_weight="balanced", max_iter=1000))
    ])

pipe.fit(textes, etiquettes)
print(pipe.predict(["salut"]))
print(pipe.predict_proba(["proba"])) # cette ligne c'est de la merde mais volontaire pour savoir ce que le bot predit quand il ne peux pas predire 

reussite = 0
foirer = 0
print("resultat de devine : \n")
for texte, attendu in zip(textes_test, etiquettes_test):
    devine = pipe.predict([texte])[0]
    if pipe.predict_proba([texte]).max() < seuilmax :
        print("\n\nje ne comprend pas : ", texte, devine, attendu)
    else :
        print(devine, pipe.predict_proba([texte]), pipe.classes_, "attendu : ", attendu)
    if devine == attendu : 
        reussite+=1
    if devine!= attendu : 
        foirer+=1

print("reussite et compagnie : ")
print("reussite : \n", reussite, "\n foirer : \n", foirer)
print(len(textes_test)) 
print((reussite / len(textes_test) * 100))

proba = cross_val_predict(pipe, textes, etiquettes, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=0), method="predict_proba")
predictions = pipe.classes_[proba.argmax(axis=1)]
confiances = proba.max(axis=1)

for attendu, devine, confiance in zip(etiquettes, predictions, confiances):
    print("attendu : ", attendu, "devine : ", devine, "confiance : ", confiance)

print(proba)