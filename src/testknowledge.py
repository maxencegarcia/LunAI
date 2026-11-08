
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