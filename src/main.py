from chatbot import Chatbot
import json
from pathlib import Path


directory_src = Path(__file__).resolve().parent.parent
chemindataintentions = directory_src / "data" / "intentions.json"
with open(chemindataintentions, encoding="utf-8") as fichier :
    intentions = json.load(fichier)

# for intention, phrases in intentions.items() :
#         print(f"{intention} : {len(phrases)} phrases")

conditionboucle = True
correctiontexte=[]
correctionetiquettes=[]

def commande(userask, lastcorrect):
    if userask == "/quit" :
        return False
    if userask == "/help" :
        print("Ecriver dans le chat et commencer par un / pour les commandes")
        print("Commande disponible : /quit /help /correction j'esperer je dois pas réellement t'expliquer ce que font ces commandes")
        return True
    if userask == "/correction" :
        possibilité = ["salutation","au_revoir","remerciement","affirmation","denegation","demande_aide","incomprehension","question","correction","salutation"]
        # print(prevrep)
        correctiontexte.append(lastcorrect)
        print("Askip je me trompe alors dis moi c'est quoi l'intentions pour (sache que tu as tord) : ", lastcorrect, "\n parmis ces choix :")
        for intention, phrases in intentions.items() :
            print(intention)
        while True:
            etiquette = input("Vas y ecrit la et vite").strip().lower()
            if etiquette in possibilité:
                correctionetiquettes.append(etiquette)
                break
            print("Tu te foutrais pas un peu de ma geule tu crois que c'est pour faire jolie que je te met des possibilité de reponse. RECOMMENCE !!!")
        correctionetiquettes.append(input())
        print("Oui oui merci pour ta correction je tacherais de m'en souvenir \n ps: si tu veux que j'enregistre ces information : /enregistre")
        print(correctionetiquettes, correctiontexte)
        return True
    if userask == "/enregistre" and correctiontexte and correctionetiquettes  :
            print("Ouais ouais je vais enregistrer c'est bon tu vas me foutre la paix ?")
            Luna.tgv(correctiontexte, correctionetiquettes)     
            correctiontexte.clear()
            correctionetiquettes.clear()  
            return True
    else : 
        print("fait un effort aprend tes commande en echange j'aprendrait l'orthographe gagnant gagnant sauf que ce que j'écrit la c'est du code brut donc il n'y auras pas de correction et toc")
        return True

Luna = Chatbot()
print("LunAI est prete")
lastcorrect =""

try:
    while conditionboucle :
        print("> ", end="")
        userask = input().strip()
        while userask == "" :
            userask = input()
        if userask.startswith("/") :
            conditionboucle = commande(userask.lower(), lastcorrect)
        else :          
            lastcorrect = userask
            print("Luna :", Luna.repondre(userask))



except KeyboardInterrupt :
    print("Interuption aurevoir")
except EOFError : 
    print("EOF aurevoir")


