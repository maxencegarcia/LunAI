import json
from pathlib import Path

def chargerexemple() :
    textes = []
    etiquettes = []
    directory_src = Path(__file__).resolve().parent.parent
    chemindataintentions = directory_src / "data" / "intentions.json"
    with open(chemindataintentions, encoding="utf-8") as fichier :
        intentions = json.load(fichier)

    for intention, phrases in intentions.items() :
            #print(f"{intention} : {len(phrases)} phrases")
            for phrases in phrases : # sus mais trkl c'est python c'est un truc pour les fous ça
                textes.append(phrases)
                etiquettes.append(intention)
    # print(len(textes),len(etiquettes),textes[:3], etiquettes[:3])
    return textes, etiquettes

def chargerexemple(chemin) :
    textes = []
    etiquettes = []
    chemin += ".json"
    directory_src = Path(__file__).resolve().parent.parent
    chemindataintentions = directory_src / "data" / chemin
    with open(chemindataintentions, encoding="utf-8") as fichier :
        intentions = json.load(fichier)

    for intention, phrases in intentions.items() :
            #print(f"{intention} : {len(phrases)} phrases")
            for phrases in phrases : # sus mais trkl c'est python c'est un truc pour les fous ça
                textes.append(phrases)
                etiquettes.append(intention)
    # print(len(textes),len(etiquettes),textes[:3], etiquettes[:3])
    return textes, etiquettes
