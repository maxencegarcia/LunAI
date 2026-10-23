import json
with open("intentions.json", encoding="utf-8") as fichier :
    intentions = json.load(fichier)

for intention, phrases in intentions.items() :
        print(f"{intention} : {len(phrases)} phrases")
