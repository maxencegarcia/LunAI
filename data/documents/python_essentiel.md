# Python : Syntaxe, Structures de Données et Pratiques de Programmation

## Introduction

Python est un langage de programmation interprété, de haut niveau, multi-paradigme et à typage dynamique. Créé par Guido van Rossum en 1991, Python est conçu autour de la philosophie du « Zen de Python » (`import this`), qui privilégie la lisibilité du code, la simplicité syntaxique et la clarté d'expression. Grâce à sa très large communauté, à sa polyvalence exceptionnelle et à sa richesse bibliothécaire, Python est le langage incontournable en science des données, en intelligence artificielle, en automatisation de scripts et en développement web.

## Fonctionnement

Le fonctionnement de Python s'appuie sur une exécution interprétée via une machine virtuelle intermédiaire. Lorsqu'un script Python (`.py`) est exécuté, l'interpréteur officiel (CPython) compile d'abord le code source en un ensemble d'instructions simplifiées appelé le bytecode Python (souvent sauvegardé sous forme de fichiers `.pyc` dans le dossier `__pycache__`).

Ensuite, la machine virtuelle CPython (PVM - Python Virtual Machine) lit et exécute ce bytecode instruction par instruction. Contrairement aux langages compilés en code natif comme C, CPython inclut un verrou d'interpréteur global appelé le GIL (Global Interpreter Lock). Le GIL empêche l'exécution simultanée de plusieurs threads Python natifs sur différents cœurs processeur dans une même instance d'interpréteur CPython, ce qui simplifie la gestion interne de la mémoire mais impose d'utiliser le multi-processus (`multiprocessing`) pour les tâches nécessitant un fort calcul parallèle sur le CPU.

La gestion de la mémoire en Python est automatique. Elle combine le comptage de références (chaque objet conserve un compteur d'allocations pointant vers lui et est détruit dès que ce compteur tombe à zéro) et un détecteur de cycles de référence capables d'identifier et de nettoyer les dépendances circulaires orphelines.

## Concepts fondamentaux

Python repose sur le principe fondamental « Tout est objet ». En Python, les nombres, les chaînes de caractères, les fonctions, les modules et les classes sont tous des objets de première classe possédant un identifiant unique, un type et une valeur.

Le typage en Python est dynamique et fort. Dynamique signifie qu'il n'est pas nécessaire de déclarer explicitement le type d'une variable lors de sa création : le type est associé à l'objet en mémoire et non à la variable elle-même. Fort signifie que Python n'effectue aucune conversion de type implicite risquée lors d'opérations entre types incompatibles (par exemple, additionner un entier et une chaîne déclenchera une erreur `TypeError`).

Les structures de données natives principales de Python incluent les listes (`list`), les tuples (`tuple`), les dictionnaires (`dict`) et les ensembles (`set`).
Les listes sont des séquences ordonnées et mutables (modifiables). Les tuples sont des séquences ordonnées mais strictement immutables, idéales pour garantir la fixité des données. Les dictionnaires sont des collections associatives de clés-valeurs hautement optimisées basées sur des tables de hachage. Les ensembles (`set`) sont des collections non ordonnées d'éléments uniques supportant les opérations mathématiques de théorie des ensembles (union, intersection, différence).

La syntaxe de Python impose l'indentation (l'alignement des espaces au début des lignes) pour délimiter les blocs de code (fonctions, conditions, boucles), remplaçant ainsi les accolades `{}` ou les mots-clés `begin/end` usités dans d'autres langages. L'indentation standard recommandée par la convention PEP 8 est de 4 espaces par niveau d'imbrication.

## Caractéristiques

Le Duck Typing ("Si cela marche comme un canard et cancane comme un canard, alors c'est un canard") est la philosophie d'interface de Python. En Python, la validité d'un objet passé à une fonction n'est pas déterminée par son héritage d'une classe spécifique, mais par la présence des méthodes et attributs requis au moment de l'exécution.

Les compréhensions de listes, de dictionnaires et d'ensembles constituent une caractéristique expressive majeure de Python. Elles permettent de générer rapidement de nouvelles collections à partir d'itérables existants via une syntaxe condensée, lisible et souvent plus rapide que des boucles `for` traditionnelles.

Les fonctions génératrices et le mot-clé `yield` permettent de produire des itérateurs paresseux (Lazy Evaluation). Au lieu de calculer et de stocker en mémoire RAM une immense liste d'éléments d'un coup, un générateur calcule et renvoie les valeurs une par une à la demande, optimisant ainsi considérablement l'empreinte mémoire lors du traitement de gros volumes de données.

## Exemples concrets

Un exemple concret de script Python illustrant la lisibilité du langage, le typage avec annotations (Type Hints), les compréhensions de listes et la manipulation de dictionnaires est fourni ci-dessous :

```python
from typing import List, Dict

def filtrer_et_bonifier_notes(notes_eleves: Dict[str, float], seuil: float) -> List[str]:
    """
    Filtre les élèves ayant une note supérieure au seuil 
    et retourne une liste de leurs noms en majuscules.
    """
    # Compréhension de liste filtrante avec transformation
    admis = [
        nom.upper() 
        for nom, note in notes_eleves.items() 
        if note >= seuil
    ]
    return admis

if __name__ == "__main__":
    promotions: Dict[str, float] = {
        "Alice": 14.5,
        "Bob": 8.0,
        "Charlie": 12.0,
        "Diana": 17.5
    }

    try:
        reussite = filtrer_et_bonifier_notes(promotions, seuil=10.0)
        print(f"Élèves admis : {reussite}")
    except TypeError as err:
        print(f"Erreur de traitement des données : {err}")
```

Un autre exemple concret est la création d'un environnement virtuel Python (`venv`) en ligne de commande. La commande `python -m venv venv_projet` crée une instance d'interpréteur isolée du système hôte, permettant d'installer des paquets tiers spécifiques via `pip install` sans risque d'entrer en conflit avec les dépendances d'autres projets ou du système d'exploitation.

## Applications

Python est le langage roi dans le domaine de l'Intelligence Artificielle, du Data Engineering et du Machine Learning grâce à des bibliothèques natives C/C++ comme NumPy (calcul matriciel), Pandas (analyse de données tabularisées), Scikit-Learn (apprentissage automatique) et PyTorch / TensorFlow (réseaux de neurones profonds).

En développement web, Python alimente des frameworks robustes tels que Django (framework haut niveau pour des applications complètes et sécurisées) et FastAPI ou Flask (micro-frameworks légers pour construire rapidement des APIs REST JSON asynchrones).

## Comparaisons

La comparaison entre les structures `list` et `tuple` repose sur la mutabilité et les performances. Une liste (`[1, 2, 3]`) est mutable : on peut y ajouter, modifier ou supprimer des éléments à chaud, ce qui nécessite une sur-allocation de mémoire dynamique et rend l'objet plus lourd. Un tuple (`(1, 2, 3)`) est immutable : une fois instancié, son contenu ne peut changer, ce qui lui confère une allocation mémoire exacte, des accès plus rapides et la capacité d'être utilisé comme clé au sein d'un dictionnaire.

La comparaison entre l'instruction `import module` et `from module import fonction` réside dans l'organisation de l'espace de nommage (Namespace). Avec `import math`, la fonction doit être appelée sous la forme `math.sqrt()`, évitant toute collision avec d'autres fonctions du programme. Avec `from math import sqrt`, la fonction est directement chargée dans l'espace de nommage courant sous le nom `sqrt()`, ce qui rend le code plus concis mais augmente le risque de masquer par inadvertance une fonction locale de même nom.

## Questions fréquentes

### Qu'est-ce que le GIL (Global Interpreter Lock) et quel est son impact sur les performances en Python ?
Le GIL est un mécanisme interne de l'interpréteur CPython qui garantit qu'un seul thread de code Python est exécuté par la PVM à un instant donné, protégeant ainsi l'état interne de l'interpréteur contre les accès concurrents non sécurisés. Son impact est qu'une application multithreadée en Python ne verra pas sa vitesse d'exécution augmenter pour des tâches nécessitant d'intensifs calculs sur le processeur (CPU-bound). Pour paralléliser des calculs lourds, il faut utiliser le module `multiprocessing` (qui lance plusieurs processus Python distincts) ou s'appuyer sur des bibliothèques C compilées qui libèrent temporairement le GIL (comme NumPy).

### Quelle est la différence entre la copie superficielle (shallow copy) et la copie profonde (deep copy) d'un objet en Python ?
Lorsqu'on effectue une copie superficielle d'un objet composé (comme une liste contenant d'autres listes via `copy.copy()`), Python crée un nouvel objet conteneur mais y insère des références vers les objets internes d'origine : modifier un sous-élément modifiera aussi l'original. Une copie profonde (réalisée via `copy.deepcopy()`) recopie récursivement tous les objets contenus à tous les niveaux d'imbrication, créant une structure totalement indépendante sans partage de références mémoires avec l'objet initial.

## Conclusion

Grâce à sa syntaxe pure et expressive, Python permet de prototyer et de développer des applications complexes rapidement. La compréhension de sa gestion dynamique des types, de la mutabilité des objets et de son écosystème de modules forme le socle essentiel pour tout développeur Python moderne.