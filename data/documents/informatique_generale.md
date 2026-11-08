# Informatique Générale : Architecture, Composants et Fonctionnement des Ordinateurs

## Introduction

L'informatique générale repose sur l'étude et l'utilisation des systèmes de traitement automatique de l'information. Un ordinateur est une machine électronique capable de recevoir des données brutes en entrée, d'effectuer des opérations arithmétiques et logiques complexes à très haute vitesse selon un ensemble d'instructions préprogrammées, et de produire des résultats exploitables en sortie. Dans le monde moderne, la maîtrise de l'architecture matérielle des ordinateurs est indispensable pour comprendre le fonctionnement des logiciels, l'optimisation des performances informatiques et l'interaction entre les composants matériels et logiciels.

## Fonctionnement

Le fonctionnement fondamental d'un ordinateur s'appuie sur le cycle d'exécution d'une instruction par le processeur, couramment appelé le cycle Fetch-Decode-Execute. Dans un premier temps, l'unité de contrôle du processeur va chercher (Fetch) l'instruction enregistrée dans la mémoire vive (RAM) à l'adresse indiquée par le pointeur d'instruction. Dans un deuxième temps, le processeur sépare le code de l'instruction en sous-éléments pour interpréter la nature de l'opération à effectuer (Decode). Enfin, le processeur exécute l'opération requise (Execute) à l'aide de son unité arithmétique et logique (ALU), puis enregistre le résultat dans des registres internes ou dans la mémoire vive avant de passer à l'instruction suivante.

La circulation des données et des instructions au sein du matériel est assurée par un réseau de lignes conductrices nommé bus informatique. Les bus système transportent les signaux d'horloge et de contrôle, les adresses mémoire indiquant où lire ou écrire, ainsi que les données réelles transférées entre le processeur, la mémoire vive et les contrôleurs de périphériques. Le rythme auquel ces opérations sont exécutées est cadencé par une horloge quartz centrale qui émet des impulsions régulières pour synchroniser l'ensemble des circuits électroniques de l'ordinateur.

## Concepts fondamentaux

L'architecture de Von Neumann est le modèle théorique standard sur lequel sont conçus la quasi-totalité des ordinateurs modernes. Proposée par le mathématicien John von Neumann, cette architecture repose sur l'utilisation d'une structure de mémoire unique stockant à la fois les données à traiter et les programmes contenant les instructions. Elle comporte quatre composants principaux : l'unité arithmétique et logique (ALU) pour les calculs, l'unité de contrôle (CU) pour le guidage des opérations, la mémoire principale pour l'enregistrement temporaire, et les unités d'entrée/sortie pour l'interaction avec le monde extérieur.

Par opposition à l'architecture de Von Neumann, l'architecture meublée dite de Harvard sépare physiquement la mémoire d'instructions de la mémoire de données. L'architecture Harvard dispose de bus de données et de bus d'adresses distincts pour chaque mémoire, ce qui permet au processeur de lire simultanément une instruction et de charger ou stocker une donnée. Cette architecture évite le goulet d'étranglement de Von Neumann, où l'accès à la mémoire unique limite la vitesse globale de traitement, et est très répandue dans les microcontrôleurs et les processeurs de traitement de signal (DSP).

Le carte mère est le circuit imprimé principal d'un ordinateur sur lequel sont connectés ou soudés tous les composants essentiels. Elle contient le socket (support du processeur), les cartes de gestion d'énergie, les stots de mémoire vive (DIMM), ainsi que le chipset (composé historiquement du pont nord et du pont sud, aujourd'hui intégrés au processeur ou résumés en un seul hub de contrôle) qui gère les liaisons à haut débit et bas débit avec la mémoire, les cartes d'extension et les périphériques de stockage.

## Caractéristiques

Les caractéristiques principales d'un ordinateur dépendent de la capacité de traitement de son processeur, de la vitesse et de la quantité de sa mémoire RAM, ainsi que du débit de ses bus de communication. La performance globale n'est pas déterminée par un seul composant mais par l'équilibre global de l'architecture hardware, évitant ainsi qu'un composant lent ne crée de goulet d'étranglement pour l'ensemble du système.

Les périphériques de stockage et d'entrée/sortie sont caractérisés par leur temps d'accès, leur bande passante (exprimée en Mo/s ou Go/s), leur capacité de stockage (en Go ou To) et leur type de connexion interface (PCIe, SATA, USB, NVMe). Par exemple, les bus de communication modernes comme le Peripheral Component Interconnect Express (PCIe) utilisent des liaisons série point-à-point ultra-rapides appelées "lignes" (lanes), qui permettent des transferts de données bidirectionnels simultanés évolutifs selon le nombre de lignes (x1, x4, x8, x16).

## Exemples concrets

Un exemple concret du fonctionnement de l'architecture matérielle d'un ordinateur survient lors du démarrage du système (processus de Boot). Lorsque l'utilisateur appuie sur le bouton d'alimentation, la carte mère reçoit du courant électrique et déclenche le micrologiciel UEFI ou BIOS gravé dans une puce de mémoire morte (ROM). L'UEFI réalise un auto-test à l'allumage (POST) pour vérifier le bon état de la RAM, de la carte graphique et des disques, puis recherche et charge le secteur d'amorçage de l'os (bootloader) depuis le SSD vers la mémoire RAM afin d'exécuter le noyau du système d'exploitation.

Un autre exemple d'interaction matérielle est le traitement d'une touche enfoncée sur un clavier mécanique USB. La touche ferme un circuit électronique sur le clavier, qui envoie un signal d'interruption matérielle au contrôleur USB de la carte mère. Le contrôleur envoie une interruption au processeur, qui interrompt temporairement son travail en cours pour traiter la frappe, charge le code de la touche (scancode) depuis le bus, puis avertit le système d'exploitation pour afficher le caractère correspondant à l'écran via la carte graphique.

## Applications

Les systèmes informatiques et leurs architectures matérielles trouvent des applications dans quasiment tous les domaines d'activité moderne. Dans les centres de données et le cloud computing, des serveurs en rack ultra-dense équipés de multiples processeurs et de disques NVMe en grappe (RAID) gèrent des téraoctets de données par seconde pour héberger des applications web et des bases de données mondiales.

Dans les systèmes embarqués et l'Internet des objets (IoT), des architectures informatiques très simplifiées comme les microcontrôleurs (par exemple basés sur ARM Cortex-M ou AVR) gèrent des capteurs de température, des robots industriels ou des calculateurs automobiles avec des contraintes strictes de consommation électrique et de traitement en temps réel.

## Comparaisons

La comparaison entre le stockage primaire (RAM) et le stockage secondaire (SSD/HDD) illustre le compromis de la hiérarchie mémoire informatique. La mémoire RAM est volatile (son contenu s'efface hors tension), offre des temps d'accès extrêmement faibles (quelques nanosecondes) et une très grande bande passante, mais coûte cher par gigaoctet. Le stockage secondaire (SSD/HDD) est non volatile (conserve les données hors tension), offre une immense capacité à coût réduit, mais possède des temps d'accès nettement plus élevés (microsecondes pour le SSD, millisecondes pour le HDD).

La comparaison entre un disque dur mécanique (HDD) et un disque à mémoire flash (SSD) réside dans le mode de lecture/écriture. Le disque dur mécanique lit des données de manière magnétique au moyen de têtes de lecture physiques sur des plateaux rotatifs, ce qui implique une fragilité mécanique et une lenteur lors des accès aléatoires. Le disque SSD conserve les données sous forme de charges électriques dans des cellules de mémoire flash NAND à semi-conducteurs, garantissant une absence totale de pièces mécaniques mobiles, une vitesse de lecture/écriture démultipliée et une grande résistance aux chocs.

## Questions fréquentes

### Quelle est la différence entre le BIOS et l'UEFI sur un ordinateur ?
Le BIOS (Basic Input/Output System) est l'ancien micrologiciel standard des cartes mères fonctionnant en mode réel 16 bits avec une limitation d'adressage des disques à 2 Téraoctets (partitionnement MBR). L'UEFI (Unified Extensible Firmware Interface) est le successeur moderne du BIOS qui s'exécute en mode 32 ou 64 bits, gère les disques de plus de 2 Téraoctets grâce au partitionnement GPT, propose une interface graphique, un temps de démarrage accéléré et inclut des fonctionnalités de sécurité renforcées comme le Secure Boot.

### Pourquoi un ordinateur a-t-il besoin de mémoire RAM en plus d'un disque dur ou d'un SSD ?
Le processeur d'un ordinateur exécute des milliards d'opérations par seconde et a besoin d'accéder aux données et instructions de façon quasi instantanée. Les disques durs et SSD, bien que rapides, sont beaucoup trop lents par rapport à la vitesse d'exécution du processeur. La mémoire RAM sert d'espace de travail temporaire ultra-rapide dans lequel le système d'exploitation charge les programmes et données en cours d'utilisation pour alimenter le processeur sans le ralentir.

## Conclusion

L'informatique générale repose sur l'assemblage cohérent de composants matériels orchestrés selon l'architecture de Von Neumann. La communication continue entre le processeur, la mémoire principale et les bus d'entrée/sortie constitue le cœur fonctionnel de tous les ordinateurs, du simple microcontrôleur embarqué au supercalculateur de recherche.