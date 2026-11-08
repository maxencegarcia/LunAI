# Shell Bash, Ligne de Commande et Administration Linux

## Introduction

Le shell Bash (Bourne-Again SHell) est l'interpréteur de commandes par défaut de la plupart des distributions Linux et des systèmes d'exploitation de type UNIX. Il sert d'interface textuelle (CLI - Command Line Interface) entre l'utilisateur (ou les scripts d'administration) et le noyau du système d'exploitation Linux. La maîtrise de la ligne de commande, des mécanismes de redirection, de la manipulation de fichiers et de la création de scripts Bash est la compétence fondamentale exigée pour tout administrateur système, ingénieur DevOps, développeur ou professionnel de la cybersécurité.

## Fonctionnement

Le fonctionnement de l'interpréteur Bash s'articule autour d'un cycle de lecture, analyse, expansion et exécution d'instructions (REPL - Read-Eval-Print Loop). Lorsque l'utilisateur saisit une ligne de commande et appuie sur la touche Entrée, Bash traite le texte entré selon une séquence stricte d'étapes :
1. Découpage en jetons (Tokenization) : découpage du texte selon les espaces et opérateurs spéciaux.
2. Expansions : remplacement des variables (`$VAR`), expansion du tilde (`~` vers le dossier personnel), expansion des chemins d'accès (Globbing avec `*` ou `?`), et substitution de commandes (ex: `$(commande)`).
3. Redirections d'entrée/sortie : configuration des flux de données standard via les symboles `<`, `>`, `>>` ou `|`.
4. Recherche de l'exécutable : vérification des alias, des fonctions internes du shell (Builtins), puis recherche du fichier binaire binaire correspondant dans les dossiers listés par la variable d'environnement `$PATH`.
5. Exécution du processus : le shell effectue un appel système `fork()` pour créer un processus enfant, suivi d'un appel système `execve()` pour lancer l'exécutable, et attend le statut de fin (`wait()`).

À la fin de l'exécution, tout programme sous Linux renvoie un code de sortie (Exit Code) compris entre 0 et 255. Un code de retour égal à `0` indique que la commande s'est exécutée avec succès sans erreur. Tout code de retour différent de 0 (par exemple `1`, `2` ou `127`) signale un échec ou un problème spécifique. Ce code est accessible immédiatement après l'exécution via la variable spéciale `$?`.

## Concepts fondamentaux

Tout processus sous Linux s'ouvre par défaut avec trois flux de données standard représentés par des descripteurs de fichiers numériques :
- Entrée standard (STDIN - Descripteur 0) : flux de lecture des données (par défaut le clavier).
- Sortie standard (STDOUT - Descripteur 1) : flux d'affichage des résultats normaux (par défaut l'écran du terminal).
- Erreur standard (STDERR - Descripteur 2) : flux d'affichage des messages d'erreur de diagnostic (par défaut l'écran du terminal).

Les opérateurs de redirection permettent de dériver ces flux vers des fichiers ou d'autres programmes.
- `>` : redirige la sortie STDOUT vers un fichier en écrasant son contenu existant.
- `>>` : redirige la sortie STDOUT en l'ajoutant (mode Append) à la fin du fichier sans l'écraser.
- `2>` : redirige spécifiquement le flux des erreurs STDERR vers un fichier.
- `&>` : redirige à la fois STDOUT et STDERR vers la même cible.
- `|` (Tube ou Pipe) : relie directement la sortie standard (STDOUT) d'une commande à l'entrée standard (STDIN) de la commande suivante, permettant d'enchaîner une suite d'outils modulaires pour former un traitement complexe.

Le système de fichiers Linux s'organise selon un arbre unique inversé partant de la racine absolue notée `/`. Les droits d'accès aux fichiers et répertoires reposent sur un modèle de sécurité à trois catégories d'utilisateurs : le Propriétaire (u - User), le Groupe propriétaire (g - Group), et les Autres (o - Others).
Pour chaque catégorie, trois types d'autorisations peuvent être attribués : la Lecture (`r`, valeur octale 4), l'Écriture (`w`, valeur octale 2) et l'Exécution (`x`, valeur octale 1). Les permissions sont modifiables via la commande `chmod` (ex: `chmod 755 fichier`).

## Caractéristiques

Les commandes Linux essentielles pour la navigation et la gestion du système incluent :
- `ls` : liste le contenu d'un répertoire (`ls -la` affiche les détails cachés et les permissions).
- `cd` : change le répertoire de travail courant.
- `pwd` : affiche le chemin d'accès absolu du répertoire de travail courant.
- `cp` / `mv` / `rm` : copie, déplace/renomme et supprime des fichiers ou dossiers (`rm -rf` supprime de manière récursive et forcée).
- `mkdir` : crée un nouveau répertoire.
- `cat` / `less` / `head` / `tail` : affichent ou naviguent dans le contenu textuel des fichiers (`tail -f` permet d'observer l'écriture des journaux système en temps réel).
- `grep` : filtre et recherche des lignes de texte correspondant à une expression régulière.
- `find` : cherche des fichiers dans l'arborescence selon des critères de nom, taille, date ou droits.
- `ps` / `top` / `htop` / `kill` : surveillent les processus en cours d'exécution et permettent de mettre fin à un processus par son identifiant (PID).

Les scripts Bash permettent d'automatiser des suites de commandes complexes. Un script commence systématiquement par la ligne "Shebang" (ex: `#!/usr/bin/env bash`) qui indique au système d'exploitation l'interpréteur à utiliser pour exécuter le script. Bash prend en charge les variables (`NOM="valeur"`), les structures conditionnelles (`if ... then ... else ... fi`), les boucles (`for`, `while`) et la déclaration de fonctions réutilisables.

## Exemples concrets

Un exemple concret de script Bash d'administration système réalisant la sauvegarde automatique d'un dossier avec horodatage, contrôle d'erreurs et nettoyage des anciennes sauvegardes est fourni ci-dessous :

```bash
#!/usr/bin/env bash

# Activation des options strictes de sécurité Bash :
# -e : arrête le script dès qu'une commande échoue
# -u : traite l'utilisation d'une variable non définie comme une erreur
# -o pipefail : renvoie le code d'erreur de la première commande échouée dans un tube (pipe)
set -euo pipefail

# Définition des variables de configuration
SOURCE_DIR="/var/www/html"
BACKUP_DIR="/var/backups/web"
DATE_JOUR=$(date +'%Y-%m-%d_%H-%M-%S')
ARCHIVE_NOM="sauvegarde_web_${DATE_JOUR}.tar.gz"

echo "=== Début du processus de sauvegarde ==="

# Vérification de l'existence du dossier source
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Erreur : Le dossier source $SOURCE_DIR n'existe pas." >&2
    exit 1
fi

# Création du répertoire de destination si nécessaire
mkdir -p "$BACKUP_DIR"

# Création de l'archive compressée
echo "Compressing $SOURCE_DIR en $ARCHIVE_NOM..."
tar -czf "${BACKUP_DIR}/${ARCHIVE_NOM}" "$SOURCE_DIR"

# Vérification du succès de la sauvegarde via le code de retour
if [ $? -eq 0 ]; then
    echo "Sauvegarde réussie : ${BACKUP_DIR}/${ARCHIVE_NOM}"
else
    echo "Erreur lors de la création de la sauvegarde !" >&2
    exit 2
fi

# Nettoyage des sauvegardes datant de plus de 7 jours
echo "Nettoyage des archives obsolètes (plus de 7 jours)..."
find "$BACKUP_DIR" -type f -name "sauvegarde_web_*.tar.gz" -mtime +7 -delete

echo "=== Sauvegarde terminée avec succès ==="
```

Un exemple de combinaison puissant de commandes en une seule ligne à l'aide des pipes est l'analyse des adresses IP qui génèrent le plus de requêtes dans un fichier journal d'un serveur web Nginx :
`cat /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 10`
Cette commande lit le journal, extrait la première colonne (les adresses IP via `awk`), trie les IP, compte le nombre d'occurrences uniques (`uniq -c`), trie les résultats par ordre numérique décroissant (`sort -nr`), et affiche les 10 adresses IP les plus actives (`head -n 10`).

## Applications

Le shell Bash et les commandes Linux sont omniprésents dans la gestion des serveurs Cloud (AWS, GCP, Azure), l'administration de conteneurs Docker, les pipelines de déploiement continu (CI/CD avec GitLab CI ou GitHub Actions), et la gestion automatisée des configurations réseau.

Ils sont également incontournables dans le secteur de la cybersécurité pour l'analyse des journaux d'évènements (Log Analysis), l'automatisation d'audits de vulnérabilités, et la réponse à des incidents de sécurité sur des serveurs distants via SSH (Secure Shell).

## Comparaisons

La comparaison entre les guillemets doubles `"` et les guillemets simples `'` en Bash est cruciale pour le traitement des variables. Les guillemets doubles (`"..."`) autorisent l'expansion des variables et des substitutions de commandes (ex: `"Bonjour $USER"` affichera `"Bonjour alice"`). Les guillemets simples (`'...'`) désactivent totalement l'interprétation par le shell et traitent le texte de façon strictement littérale (ex: `'Bonjour $USER'` affichera exactement `'Bonjour $USER'`).

La comparaison entre un chemin relatif et un chemin absolu détermine comment le système localise une ressource. Un chemin absolu part obligatoirement de la racine du système (`/`) et identifie un fichier de manière unique, quel que soit l'emplacement de l'utilisateur (ex: `/etc/nginx/nginx.conf`). Un chemin relatif dépend du dossier courant dans lequel l'utilisateur se trouve actuellement (ex: `./config/app.json` ou `../images/logo.png`).

## Questions fréquentes

### Que signifie l'erreur "Permission denied" (Permission refusée) lors de l'exécution d'une commande Linux ?
L'erreur "Permission denied" se produit lorsque le compte utilisateur courant qui lance la commande ne dispose pas des droits de sécurité nécessaires sur le fichier ou répertoire visé (droit de lecture `r`, d'écriture `w` ou d'exécution `x`). Pour résoudre ce problème, l'utilisateur doit soit être le propriétaire du fichier et modifier ses droits avec `chmod`, soit élever temporairement ses privilèges administrateur en préfixant la commande du mot-clé `sudo` (SuperUser DO), sous réserve de posséder les droits d'administration dans le fichier `/etc/sudoers`.

### Quelle est la différence entre un lien physique (Hard Link) et un lien symbolique (Soft Link / Symlink) sous Linux ?
Un lien physique (Hard Link) est un deuxième nom attribué qui pointe directement vers le même numéro d'index physique (i-node) sur le disque dur : si l'on supprime le fichier d'origine, les données restent accessibles via le lien physique. Un lien symbolique (`ln -s source cible`) est un fichier spécial très léger contenant simplement une référence texte pointant vers le chemin d'accès d'un autre fichier : si le fichier d'origine est supprimé ou déplacé, le lien symbolique devient orphelin ("cassé") et ne fonctionne plus.

## Conclusion

Le shell Bash et les commandes Linux représentent un langage d'automatisation puissant et indispensable. La maîtrise de la gestion des descripteurs de flux, de l'arborescence des fichiers, des autorisations de sécurité et de la création de scripts autonomes est au cœur de l'administration et du développement informatique moderne.