from intent_classifier import IntentClassifier



class Chatbot :
    def __init__(self):
        self.clf = IntentClassifier()
        self.clf.load("Lunav1")

    def repondre(self, message) -> str :
        intention,confiance = self.clf.predire(message)
        return intention, confiance

