from intent_classifier import IntentClassifier
from personality import reppourinconnue
from personality import reppoursalutation
from personality import reppourincorteshearsh
from personality import reppourreshearsh
from personality import reppourremerciement
from personality import reppouraurevoir
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import pygame
from pathlib import Path
from knowledge import Knowledge
import sys
directory_src = Path(__file__).resolve().parent.parent
chemin_rihanna = directory_src / "data" / "Rihanna"
sys.path.append(str(chemin_rihanna))
import Rihannainfo



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
        if intention == "au_revoir" :
            return reppouraurevoir()
        if intention == "remerciement" :
            return reppourremerciement    
        if intention == "question" or intention == "demande_aide":
            resultats = self.know.chercher(message, 1, 0.18)
            if resultats == "inconnue":
                return reppourincorteshearsh()
            return reppourreshearsh(resultats)
        return intention, confiance

    def addallknowledgetempo(self) :
        self.know.connexion() # a verif si je garde ça
        self.know.ajouter_document("processeurs.md")
        self.know.ajouter_document("memoire.md")
        self.know.ajouter_document("informatique_generale.md")
        self.know.ajouter_document("cybersecurit.md")
        self.know.ajouter_document("c_essentiel.md")
        self.know.ajouter_document("java_essentiel.md")
        self.know.ajouter_document("python_essentiel.md")
        self.know.ajouter_document("bash_linux.md")
        self.know.ajouter_document("reseaux.md")

def playrihanna() :
    directory_src = Path(__file__).resolve().parent.parent
    chemindatasong = directory_src / "data" / "Rihanna" / "OGR.mp3"   
    pygame.mixer.init()
    pygame.mixer.music.load(str(chemindatasong))
    pygame.mixer.music.play()
    print("Vas y gamin profite")
    return True


def infoRihanna() :
    print(Rihannainfo.rihannainfo())