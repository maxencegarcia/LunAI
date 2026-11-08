import sqlite3
import hashlib
from pathlib import Path
from contextlib import contextmanager


class Knowledge :
    def __init__(self, chemindb = None):
        racine = Path(__file__).resolve().parent.parent
        if chemindb is None :
            chemindb = "chatbot.db"
        chemin = racine / "data" / chemindb 
        print(chemin)
        self.chemindb = str(chemin)
        self.initialiserdb()


    @contextmanager # pour le yield et le with ensemble 
    def connexion(self) : 
        conn = sqlite3.connect(self.chemindb)
        conn.execute("PRAGMA foreign_keys = ON") # sinon askip il y a des erreur donc bon on le fait pis voila quoi
        try:
            yield conn # de ce que je sais ça renvoiue une sorte de return assez bizard mais bon c'est du sql je deteste ça et je ne suis pas assez payé (etendis que je ne suis pas payé du tout) pour reflechir a ça
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
   
    def initialiserdb(self) :
        with self.connexion() as conn: 
            conn.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    chemin TEXT NOT NULL UNIQUE,
                    empreinte TEXT NOT NULL,
                    date_import TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS passages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document_id INTEGER NOT NULL,
                    numero INTEGER NOT NULL,
                    texte TEXT NOT NULL,

                    FOREIGN KEY (document_id)
                    REFERENCES documents(id)
                    ON DELETE CASCADE,

                    UNIQUE(document_id, numero)
                )
            """)

    def decouper_document(self, contenu):    
            passages = contenu.split("\n\n")
            return [passage.strip() for passage in passages if passage.strip()]

    def calculer_empreinte(self, contenu):
        """Calcule une empreinte pour détecter les modifications."""

        return hashlib.sha256(
            contenu.encode("utf-8")
        ).hexdigest()

    def ajouter_document(self, chemin):
        racine = Path(__file__).resolve().parent.parent
        chemindoc = racine / "data" / "documents" / chemin
        chemin = chemindoc
        chemin = Path(chemin).resolve()
        print(chemin)

        if not chemin.exists():
            print("ça existe pas ton document la regarde mieux")
            return

        if chemin.suffix.lower() not in [".md", ".txt"]:
            print("bonsoir je prend que .md ou .txt donc Maxence merci d'aller te faire avec ton extension bizarre ou alors ta faute de frappe")
            return
        
        contenu = chemin.read_text(encoding="utf-8")
        passages = self.decouper_document(contenu)
        empreinte = self.calculer_empreinte(contenu)

        if not passages:
            print("t'essaye pas de m'anarquer avec ton document vide la ?")
            return False

        with self.connexion() as conn:
            curseur = conn.execute(
                "SELECT id, empreinte FROM documents WHERE chemin = ?",
                (str(chemin),)
            )

            document = curseur.fetchone()


            if document:
                document_id, ancienne_empreinte = document
                # si pas changement
                if ancienne_empreinte == empreinte:
                    print("Document déjà importé et inchangé.")
                    return False

                # si changement
                conn.execute(
                    """
                    UPDATE documents
                    SET nom = ?, empreinte = ?,
                        date_import = CURRENT_TIMESTAMP
                    WHERE id = ?
                    """,
                    (chemin.name, empreinte, document_id)
                )

                conn.execute(
                    "DELETE FROM passages WHERE document_id = ?",
                    (document_id,)
                )

            else:

                curseur = conn.execute(
                    """
                    INSERT INTO documents (nom, chemin, empreinte)
                    VALUES (?, ?, ?)
                    """,
                    (chemin.name, str(chemin), empreinte)
                )

                document_id = curseur.lastrowid

            # Enregistrement
            for numero, texte in enumerate(passages, start=1):

                conn.execute(
                    """
                    INSERT INTO passages
                    (document_id, numero, texte)
                    VALUES (?, ?, ?)
                    """,
                    (document_id, numero, texte)
                )

        print("c'est bon voila le nombre Bisous :heart: :", len(passages))

        return True

    def lister_documents(self):
        with self.connexion() as conn:

            curseur = conn.execute("""
                SELECT id, nom, date_import
                FROM documents
                ORDER BY nom
            """)

            return curseur.fetchall()

    def lister_passages(self, document_id):
        with self.connexion() as conn:

            curseur = conn.execute("""
                SELECT numero, texte
                FROM passages
                WHERE document_id = ?
                ORDER BY numero
            """, (document_id,))

            return curseur.fetchall()

    def rechercher(self, mot_cle):
        with self.connexion() as conn:

            curseur = conn.execute("""
                SELECT documents.nom, passages.numero, passages.texte
                FROM passages
                JOIN documents
                    ON documents.id = passages.document_id
                WHERE passages.texte LIKE ?
                ORDER BY documents.nom, passages.numero
            """, (f"%{mot_cle}%",))

            return curseur.fetchall()
