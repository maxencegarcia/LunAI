from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from dataloader import chargerexemple
textes, etiquettes = chargerexemple()
textes_test, etiquettes_test = chargerexemple("testsimpleintention")

pipe = Pipeline([
    ("vecteuri", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,5))),
    ("classi", LogisticRegression(class_weight="balanced", max_iter=1000))
    ])

pipe.fit(textes, etiquettes)
print(pipe.predict(["salut"]))
print(pipe.predict_proba(["proba"]))

reussite = 0
print("resultat de devine : \n")
for texte, attendu in zip(textes_test, etiquettes_test):
    devine = pipe.predict([texte])[0]
    print(devine, "attendu : ", attendu)
    if devine == attendu : 
        reussite+=1

print("reussite et compagnie : ")
print(reussite)
print(len(textes_test)) 
print((reussite / len(textes_test) * 100))