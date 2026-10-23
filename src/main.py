from chatbot import Chatbot
import json
from pathlib import Path


directory_src = Path(__file__).resolve().parent.parent
chemindataintentions = directory_src / "data" / "intentions.json"
with open(chemindataintentions, encoding="utf-8") as fichier :
    intentions = json.load(fichier)

for intention, phrases in intentions.items() :
        print(f"{intention} : {len(phrases)} phrases")

conditionboucle = True

def commande(userask):
    if userask == "/quit" :
        return False
    if userask == "/help" :
        print("ecriver dans le chat et commencer par un / pour les commandes")
        print("commande disponible : /quit /help")
        return True
    else : 
        print("fait un effort aprend tes commande en echange j'aprendrait l'orthographe gagnant gagnant sauf que ce que j'écrit la c'est du code brut donc il n'y auras pas de correction et toc")
        return True

Luna = Chatbot()
print("LunAI est prete")

try:
    while conditionboucle :
        print("> ", end="")
        userask = input().strip()
        while userask == "" :
            userask = input()
        if userask.startswith("/") :
            conditionboucle = commande(userask.lower())
        else :
            print("Luna :",Luna.repondre(userask))



except KeyboardInterrupt :
    print("Interuption aurevoir")
except EOFError : 
    print("EOF aurevoir")


