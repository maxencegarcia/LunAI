
from knowledge import Knowledge

# Initialisation de la base
kb = Knowledge()

# Import d'un document
kb.ajouter_document("reseaux.md")

# Afficher les documents importés
print("\n--- DOCUMENTS ---")

for document in kb.lister_documents():
    print(document)

# Afficher les passages du premier document
print("\n--- PASSAGES ---")

for numero, texte in kb.lister_passages(1):
    print(f"\nPassage {numero} :")
    print(texte)

# Tester une recherche
print("\n--- RECHERCHE ---")

resultats = kb.rechercher("fonctionnement")

for nom, numero, texte in resultats:
    print(f"\n{nom} | Passage {numero}")
    print(texte)

# import des autre doc ouais c fait comme de la merde et alors ?
kb.ajouter_document("processeurs.md")
kb.ajouter_document("memoire.md")
kb.ajouter_document("informatique_generale.md")
kb.ajouter_document("cybersecurit.md")
kb.ajouter_document("c_essentiel.md")
kb.ajouter_document("java_essentiel.md")
kb.ajouter_document("python_essentiel.md")
kb.ajouter_document("bash_linux.md")

print("\n--- DOCUMENTS ---")
for document in kb.lister_documents():
    print(document)


tous = kb.retourntoutpassage()
print(len(tous))
print(tous[0])


print("\n--- RECHERCHE TF-IDF ---")

question1 = "Pourquoi mon script n'accélère pas vraiment quand j'essaie de répartir des calculs lourds sur plusieurs threads en même temps ?"

resultats = kb.chercher(question1, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")

question2 = "Comment se fait-il que la RAM de mon système finisse par saturer si je ne détruis pas manuellement les variables dont je n'ai plus besoin ?"

question3 = "Dois-je générer un exécutable différent si je veux faire tourner mon programme à la fois sur un serveur Linux et sur mon poste Windows ?"
question4 = "Quelle est la méthode pour filtrer le résultat d'une commande et n'enregistrer que ses messages d'erreur dans un fichier, en ignorant le fonctionnement normal ?"
question5 = "Comment mon ordinateur parvient-il à trouver la bonne machine cible sur internet quand je tape un simple nom de site web au lieu d'une suite de chiffres ?"

questionhs1 = "Quel est le temps de cuisson exact pour obtenir un œuf mollet avec le jaune encore coulant ?"
questionhs2 = "Comment fonctionne le barème progressif de l'impôt sur le revenu en France ?"
questionhs3 = "Quels sont les meilleurs exercices pour améliorer son endurance fondamentale en course à pied ?"
questionhs4 = "Qui a composé la bande originale du film Interstellar ?"
questionhs5 = "Pourquoi les feuilles des arbres perdent-elles leur couleur verte pour devenir jaunes ou rouges en automne ?"

resultats = kb.chercher(question2, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")

resultats = kb.chercher(question3, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")

resultats = kb.chercher(question4, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")


resultats = kb.chercher(question5, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")

resultats = kb.chercher(questionhs1, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")


resultats = kb.chercher(questionhs2, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")

resultats = kb.chercher(questionhs3, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")
    
resultats = kb.chercher(questionhs4, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")

resultats = kb.chercher(questionhs5, k=3)

for score, nom, numero, texte in resultats:
    print(f"\nDocument : {nom}")
    print(f"Passage : {numero}")
    print(f"Score : {score:.4f}")
    print(f"Texte : {texte}")



# expected
# q1 : doc : python_essentiel.md, passage : 31
# q2 : doc : c.md, passage : (non trouvé dans l'extrait)
# q3 : doc : java.md, passage : (non trouvé dans l'extrait)
# q4 : doc : bash_linux.md, passage : (non trouvé dans l'extrait)
# q5 : doc : reseaux.md, passage : 19