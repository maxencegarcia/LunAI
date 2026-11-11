from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import StratifiedKFold
from dataloader import chargerexemple
from pathlib import Path
import joblib


class IntentClassifier :
    def __init__(self, seuil=0.40): # ex 0.20
        self.seuil = seuil
        self.pipe = Pipeline([
        ("vecteuri", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,5))),
        ("classi", LogisticRegression(C=10, class_weight="balanced", max_iter=1000))
        ])
        self.entrainer = False



    def train(self, textes, etiquettes) :
    #    textes, etiquettes = chargerexemple()
        self.pipe.fit(textes, etiquettes)
        self.entrainer = True
#avant c'est train donc la c'est tgv je suis marrant hein ?
# au moi du futur c'est pour rentrainé avec une correction
    def tgv(self, textecorrigé, etiquettecorrigé) :
        textes, etiquettes = chargerexemple()
        for i in range(0, len(textecorrigé))  :
            textes.append(textecorrigé[i])
            etiquettes.append(etiquettecorrigé[i])
        self.pipe.fit(textes, etiquettes)
        self.entrainer = True


    def predire(self, texte):
        if not self.entrainer :
            raise RuntimeError("le modele n'est pas entrainer ou alors il y a rien de charger jsp demerder vous vous mais il faut faire un des 2 ou les 2 Zut ! ")
        proba = self.pipe.predict_proba([texte])[0]
        i = proba.argmax()
        confiance = float(proba[i]) # sinon on vas galerer a conparer au seuil
        #seuilactu = self.pipe.predict_proba([texte]).max()
        #predictions = self.pipe.classes_[seuilactu.argmax(axis=1)]
        if confiance < self.seuil :
            return "inconnue", confiance
        return str(self.pipe.classes_[i]), confiance

    def save(self, nom) : 
        directory_src = Path(__file__).resolve().parent.parent
        nom+=".joblib"
        cheminmodelLuna = directory_src / "models" / nom
        joblib.dump(self.pipe, cheminmodelLuna )

    def load(self, nom) : 
        directory_src = Path(__file__).resolve().parent.parent
        nom+=".joblib"
        cheminmodelLuna = directory_src / "models" / nom
        self.pipe = joblib.load(cheminmodelLuna)
        self.entrainer = True





