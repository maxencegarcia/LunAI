from intent_classifier import IntentClassifier
from personality import reppourinconnue



class Chatbot :
    def __init__(self):
        self.clf = IntentClassifier()
        self.clf.load("Lunav1")

    def repondre(self, message) -> str :
        intention,confiance = self.clf.predire(message)
        if intention == "inconnue" :
            return reppourinconnue()
        return intention, confiance

