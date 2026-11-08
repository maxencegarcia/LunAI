# Cybersécurité : Principes, Cryptographie, Authentification et Protection

## Introduction

La cybersécurité est la discipline informatique visant à protéger les systèmes, réseaux, programmes, équipements et données contre les attaques numériques, les accès non autorisés, les altérations ou la destruction. Dans un monde interconnecté où la quasi-totalité des activités économiques, administratives et personnelles dépend d'infrastructures informatiques, la cybersécurité est devenue une composante stratégique majeure. Comprendre les piliers de la sécurité, les mécanismes d'attaque, les solutions cryptographiques et les meilleures pratiques d'ingénierie est essentiel pour bâtir des environnements technologiques résilients.

## Fonctionnement

La défense en profondeur (Defense in Depth) est le principe fondamental du fonctionnement de la cybersécurité moderne. Elle stipule qu'aucune mesure de protection individuelle n'est totalement infaillible. Par conséquent, la sécurité d'un système doit être construite en imbriquant plusieurs couches de protections indépendantes et complémentaires. Si un attaquant parvient à franchir une barrière extérieure (par exemple en contournant un pare-feu réseau), les couches de protection suivantes (comme le chiffrement des bases de données, le contrôle d'accès utilisateur et la détection d'intrusions applicative) l'empêcheront d'atteindre et d'exfiltrer les données sensibles.

Le fonctionnement d'une attaque informatique type suit généralement la méthodologie de la chaîne de destruction cyber (Cyber Kill Chain). L'attaquant commence par une phase de reconnaissance (collecte d'informations), suivie de la préparation de l'attaque (Weaponization), de la livraison de la charge utile (ex: email de phishing), de l'exploitation d'une vulnérabilité système, de l'installation du logiciel malveillant (malware), de l'établissement d'un canal de commande et contrôle (C2), et enfin de l'exécution des actions malveillantes (vol de données, chiffrement par ransomware ou sabotage).

## Concepts fondamentaux

La CIA Triad (Confidentialité, Intégrité, Disponibilité) constitue le modèle théorique universel de la sécurité de l'information. La Confidentialité garantit que les données ne sont accessibles qu'aux personnes ou processus dûment autorisés. L'Intégrité garantit que les données n'ont été ni altérées, ni modifiées, ni détruites de manière accidentelle ou malveillante. La Disponibilité garantit que les systèmes d'information et les données restes accessibles aux utilisateurs légitimes aux moments où ils en ont besoin. Dans de nombreuses normes modernes, s'ajoutent la Traçabilité (Non-répudiation) et l'Authenticité.

Le chiffrement symétrique est un mécanisme cryptographique où une seule et même clé secrète est utilisée à la fois pour chiffrer le message lisible en texte chiffré et pour déchiffrer le texte chiffré en message lisible. Les algorithmes symétriques modernes, tels que l'AES (Advanced Encryption Standard) avec des clés de 128 ou 256 bits, offrent une vitesse de traitement extrêmement rapide pour chiffrer de gros volumes de données mais posent le défi du partage sécurisé de la clé secrète initiale entre les interlocuteurs.

Le chiffrement asymétrique (ou cryptographie à clé publique) utilise une paire de clés mathématiquement liées : une clé publique, qui peut être partagée ouvertement à tout le monde, et une clé privée, qui doit être conservée strictement secrète par son propriétaire. Une donnée chiffrée avec la clé publique ne peut être déchiffrée que par la clé privée correspondante. Les algorithmes asymétriques populaires incluent RSA et la cryptographie sur les courbes elliptiques (ECC).

L'authentification multifacteur (MFA - Multi-Factor Authentication) est une méthode de contrôle d'accès exigeant qu'un utilisateur fournisse au moins deux preuves d'identité distinctes appartenant à des catégories différentes avant d'obtenir un accès. Ces catégories sont : ce que l'on sait (mot de passe, code PIN), ce que l'on possède (clé physique d'authentification, application OTP sur smartphone), et ce que l'on est (empreinte digitale, reconnaissance faciale).

Le pare-feu (Firewall) est un dispositif matériel ou logiciel filtrant les flux de données entrant et sortant d'un réseau ou d'un ordinateur. Le pare-feu analyse les paquets réseau par rapport à un jeu de règles de sécurité prédéfinies (ex: autoriser le trafic entrant sur le port 443 HTTPS mais bloquer le port 22 SSH en provenance d'Internet public) afin d'isoler les zones de confiance des zones non sécurisées.

## Caractéristiques

Une fonction de hachage cryptographique (ex: SHA-256) est un algorithme mathématique à sens unique (unidirectionnel) qui transforme n'importe quel bloc de données en entrée de taille variable en une empreinte numérique (hash) de longueur fixe. Les propriétés clés d'un hachage cryptographique robuste sont la résistance aux préimages (impossible de retrouver l'entrée initiale à partir du hash), la résistance aux secondes préimages, et la résistance aux collisions (il doit être informatiquement impossible de trouver deux entrées différentes produisant la même empreinte).

Les vulnérabilités logicielles sont des failles ou défauts de conception dans un programme permettant à un attaquant de s'octroyer des privilèges indus ou d'exécuter du code non autorisé. Les vulnérabilités reconnues sont répertoriées au niveau mondial sous forme d'identifiants CVE (Common Vulnerabilities and Exposures) et évaluées selon une échelle de gravité normalisée appelée CVSS (Common Vulnerability Scoring System) allant de 0.0 (négligeable) à 10.0 (critique).

## Exemples concrets

Un exemple concret d'attaque web courante est l'injection SQL (SQL Injection). Si une application web ne nettoie ni ne valide les entrées saisies par un utilisateur dans un champ de formulaire de connexion, un attaquant peut injecter du code SQL malveillant (comme `' OR '1'='1`). Le serveur de base de données interprète alors l'entrée comme une instruction valide et renvoie les données de tous les utilisateurs, contournant totalement l'authentification par mot de passe.

Un exemple d'application de la cryptographie asymétrique est la signature numérique d'un logiciel. Un éditeur de logiciels génère l'empreinte hachée de son exécutable et la chiffre avec sa clé privée. Tout utilisateur téléchargeant le logiciel utilise la clé publique de l'éditeur pour déchiffrer la signature et la comparer au hachage du fichier téléchargé : si les empreintes correspondent, l'utilisateur a la garantie absolue que le logiciel provient bien de l'éditeur et n'a pas été corrompu par un virus lors du téléchargement.

## Applications

Dans les architectures informatiques d'entreprise modernes, l'approche Zero Trust ("Ne jamais faire confiance, toujours vérifier") remplace le modèle traditionnel du périmètre réseau sécurisé. Dans une architecture Zero Trust, aucun utilisateur ni aucun équipement, qu'il soit situé à l'intérieur ou à l'extérieur du réseau de l'entreprise, ne bénéficie d'une confiance implicite. Chaque demande d'accès à une ressource applicative doit être réauthentifiée, réautorisée et chiffrée en continu.

Les systèmes de détection et de prévention d'intrusions (IDS/IPS) et les outils EDR (Endpoint Detection and Response) analysent en temps réel les journaux d'évènements, la mémoire, les appels système et les connexions réseau afin de détecter des comportements anormaux évocateurs d'une infection ou d'une exfiltration de données, et d'isoler automatiquement les machines compromises.

## Comparaisons

La comparaison entre chiffrement symétrique et chiffrement asymétrique met en évidence leur complémentarité dans les protocoles modernes comme TLS/HTTPS. Le chiffrement asymétrique est très coûteux en ressources de calcul mais permet d'échanger de façon sécurisée une clé secrète temporaire entre deux inconnus à travers un réseau public. Le chiffrement symétrique prend ensuite le relais pour chiffrer à ultra-haute vitesse l'ensemble de la session de communication avec cette clé partagée.

La comparaison entre le chiffrement et le hachage réside dans la réversibilité de l'opération. Le chiffrement est une opération bidirectionnelle conçue pour masquer le contenu d'un message afin qu'il puisse être déchiffré ultérieurement au moyen d'une clé. Le hachage est une opération unidirectionnelle irréversible destinée à calculer l'empreinte d'intégrité d'un contenu sans intention de reconstruire l'original à partir de l'empreinte.

## Questions fréquentes

### Pourquoi est-il dangereux d'utiliser des fonctions de hachage obsolètes comme MD5 ou SHA-1 ?
Les algorithmes MD5 et SHA-1 sont aujourd'hui considérés comme complètement cassés sur le plan cryptographique car les chercheurs ont démontré qu'il est possible de générer artificiellement des collisions (deux fichiers complètement différents produisant la même empreinte MD5 ou SHA-1) en un temps de calcul très court. Un attaquant pourrait ainsi substituer un fichier malveillant à un document légitime sans modifier l'empreinte de contrôle. Il est impératif d'utiliser aujourd'hui la famille SHA-2 (ex: SHA-256) ou SHA-3.

### Qu'est-ce qu'une attaque par Ingénierie Sociale (Social Engineering) et Phishing ?
L'ingénierie sociale désigne l'ensemble des techniques de manipulation psychologique visant à inciter des personnes à accomplir des actes dangereux ou à divulguer des informations confidentielles. Le phishing (hameçonnage) en est la forme la plus répandue via l'envoi d'emails frauduleux usurpant l'identité d'entreprises ou de collègues de confiance pour inciter la victime à cliquer sur un lien piégé, saisir ses identifiants sur une fausse page Web ou exécuter une pièce jointe malveillante.

## Conclusion

La cybersécurité repose sur l'équilibre entre la rigueur de la cryptographie, la défense multi-couches, l'application continue des correctifs logiciels et la sensibilisation humaine. Face au développement permanent des menaces et des failles d'exploitation, la sécurité doit être conçue dès l'origine dans tout système informatique selon le principe de la sécurité par conception (Security by Design).