from intent_classifier import IntentClassifier
from personality import reppourinconnue
from personality import reppoursalutation
from personality import reppourincorteshearsh
from personality import reppourreshearsh
from knowledge import Knowledge



class Chatbot :
    def __init__(self):
        self.clf = IntentClassifier()
        self.know = Knowledge()
        self.addallknowledgetempo()
        self.clf.load("Lunav1")

    def repondre(self, message) -> str :
        intention,confiance = self.clf.predire(message)
        if intention == "inconnue" :
            return reppourinconnue()
        if intention == "salutation" :
            return reppoursalutation()
        if intention == "question" or intention == "demande_aide":
            research = self.know.chercher(message, 1, 0.18)
            if(research == "inconnue") :
                return reppourincorteshearsh()
            else :
                return reppourreshearsh(research)
        return intention, confiance

    def addallknowledgetempo(self) :
        self.know.ajouter_document("processeurs.md")
        self.know.ajouter_document("memoire.md")
        self.know.ajouter_document("informatique_generale.md")
        self.know.ajouter_document("cybersecurit.md")
        self.know.ajouter_document("c_essentiel.md")
        self.know.ajouter_document("java_essentiel.md")
        self.know.ajouter_document("python_essentiel.md")
        self.know.ajouter_document("bash_linux.md")
        self.know.ajouter_document("reseaux.md")