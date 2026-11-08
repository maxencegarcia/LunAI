# Réseaux Informatiques : TCP/IP, Protocole, Adressage et Services

## Introduction

Un réseau informatique est un ensemble d'équipements électroniques (ordinateurs, serveurs, routeurs, commutateurs) reliés entre eux par des supports physiques (câbles cuivre, fibre optique) ou hertziens (Wi-Fi, liaisons satellite) afin de communiquer et d'échanger des données numériques. Les réseaux constituent l'infrastructure fondamentale d'Internet, de l'interconnexion des entreprises et du fonctionnement du Cloud. Comprendre l'architecture des réseaux, les modèles en couches, les mécanismes d'adressage et les protocoles majeurs est primordial pour l'administration système, la programmation et la cybersécurité.

## Fonctionnement

Le fonctionnement d'un réseau informatique s'appuie sur le principe de la commutation de paquets. Lorsqu'une information volumineuse (comme une image ou un fichier texte) doit être transmise d'une machine cliente à un serveur distant, elle est découpée au niveau de la couche transport en plusieurs segments ou paquets de données de taille réduite. Chaque paquet est encapsulé en y ajoutant des en-têtes contenant les adresses d'origine, les adresses de destination, ainsi que des informations de contrôle et de vérification d'erreurs (checksum).

Ces paquets voyagent ensuite indépendamment à travers un maillage de routeurs d'interconnexion. Les routeurs examinent l'adresse IP de destination contenue dans l'en-tête de chaque paquet et consultent leurs tables de routage pour déterminer le chemin physique le plus optimal vers le réseau suivant. À la réception, la machine destinataire procède au désencapsulage des paquets, vérifie leur intégrité, les réordonne si nécessaire et réassemble l'information initiale pour la présenter à l'application destinataire.

## Concepts fondamentaux

Le modèle OSI (Open Systems Interconnection) est un modèle conceptuel normalisé décrivant les communications réseau en 7 couches d'abstraction distinctes : la couche Physique (1), la couche Liaison de données (2), la couche Réseau (3), la couche Transport (4), la couche Session (5), la couche Présentation (6) et la couche Application (7). Chaque couche s'appuie sur les services offerts par la couche inférieure et propose des fonctionnalités standardisées à la couche supérieure.

Le modèle TCP/IP est l'architecture concrète et opérationnelle appliquée sur Internet. Plus synthétique que le modèle OSI, le modèle TCP/IP comprend 4 couches principales : la couche Accès réseau (équivalant aux couches 1 et 2 OSI), la couche Internet (couche 3 OSI), la couche Transport (couche 4 OSI) et la couche Application (regroupant les couches 5, 6 et 7 OSI).

L'adresse IP (Internet Protocol) est un identifiant numérique attribué à chaque interface d'un équipement connecté à un réseau informatique utilisant l'Internet Protocol. L'adressage IPv4 utilise des adresses de 32 bits notées sous forme de quatre nombres décimaux séparés par des points (ex: `192.168.1.1`), offrant environ 4,3 milliards d'adresses. Pour contrer la pénurie d'adresses IPv4, le protocole IPv6 a été développé, utilisant un adressage de 128 bits noté en hexadécimal (ex: `2001:0db8:85a3::8a2e:0370:7334`), offrant un nombre d'adresses virtuellement illimité.

Les ports de communication sont des numéros logiques codés sur 16 bits (de 0 à 65535) associés à une adresse IP pour identifier un service ou un processus applicatif précis sur une machine. Par exemple, le port 80 est réservé par convention au protocole HTTP non sécurisé, le port 443 au protocole HTTPS sécurisé, le port 22 au protocole SSH d'administration à distance, et le port 53 au service de résolution DNS.

## Caractéristiques

Le protocole TCP (Transmission Control Protocol) est un protocole de la couche transport orienté connexion. TCP garantit que toutes les données transmises arrivent à destination sans altération, sans doublon et strictement dans l'ordre d'émission. Pour assurer cette fiabilité, TCP établit une liaison préalable via un mécanisme de poignée de main en trois temps (TCP 3-Way Handshake : SYN, SYN-ACK, ACK), utilise des accusés de réception (ACK) et réémet automatiquement les paquets perdus.

Le protocole UDP (User Datagram Protocol) est un protocole de la couche transport non orienté connexion et non fiable. UDP envoie des paquets de données (datagrammes) à un destinataire sans vérifier au préalable si le destinataire est prêt et sans demander d'accusé de réception. UDP offre une latence extrêmement faible et une vitesse d'émission maximale au détriment de la garantie de livraison, ce qui en fait le choix privilégié pour le streaming vidéo en direct, le jeu vidéo en ligne et les requêtes DNS.

Le système DNS (Domain Name System) est le service de l'annuaire distribué d'Internet. Le protocole DNS traduit les noms de domaine lisibles par les êtres humains (tels que `www.exemple.com`) en adresses IP numériques intelligibles par les équipements réseau (telles que `93.184.216.34`), permettant ainsi aux navigateurs web d'établir les connexions adéquates.

Le protocole DHCP (Dynamic Host Configuration Protocol) est un service réseau qui attribue automatiquement et de manière dynamique les paramètres d'adressage IP aux équipements clients rejoignant un réseau local. Lors de sa connexion, une machine émet une requête DHCP pour obtenir une adresse IP disponible, un masque de sous-réseau, l'adresse de la passerelle par défaut et les adresses des serveurs DNS du réseau.

Le protocole HTTP (Hypertext Transfer Protocol) et sa version sécurisée HTTPS (HTTP Secure) sont des protocoles d'application client-serveur utilisés pour la transmission de documents hypertexte et de web APIs. Le protocole HTTPS encapsule les échanges HTTP standards au sein d'une couche d'en-tête de chiffrement TLS (Transport Layer Security), garantissant ainsi la confidentialité des données, l'intégrité des échanges et l'authentification du serveur web distant via un certificat numérique.

## Exemples concrets

Un exemple concret du déroulement d'une requête web se produit lorsqu'un utilisateur saisit `https://www.exemple.com` dans son navigateur web. D'abord, l'ordinateur interroge son serveur DNS pour obtenir l'adresse IP associée au nom `www.exemple.com`. Une fois l'adresse IP obtenue, une connexion TCP est ouverte sur le port 443 du serveur distant via la poignée de main SYN / SYN-ACK / ACK. Ensuite, une session TLS est négociée pour échanger des clés de chiffrement symétriques. Enfin, le navigateur envoie une requête HTTP `GET /`, et le serveur web retourne le code source HTML de la page web demandée.

Un autre exemple concret est le fonctionnement du sous-réseau et de la passerelle par défaut en entreprise. Une machine possédant l'adresse IP `192.168.1.15` avec un masque de sous-réseau `/24` (`255.255.255.0`) souhaite contacter l'adresse `192.168.1.50`. Le système constate que l'hôte cible se trouve sur le même sous-réseau local et envoie directement la trame sur le commutateur (Switch) grâce au protocole ARP (Address Resolution Protocol). Si la machine cible avait été l'adresse publique `8.8.8.8`, la machine aurait transmis le paquet à l'adresse de sa passerelle par défaut (le routeur local) pour qu'il soit routé vers le réseau externe.

## Applications

Les architectures réseaux sont utilisées dans les infrastructures web d'entreprise avec la mise en œuvre de pare-feu (Firewalls), de serveurs Proxy, de réseaux privés virtuels (VPN) et de répartiteurs de charge (Load Balancers). Le Load Balancer répartit le trafic entrant provenant de milliers d'utilisateurs sur une ferme de serveurs d'applications web afin d'éviter la saturation d'un équipement unique et d'assurer une haute disponibilité du service.

Dans le cadre des réseaux locaux d'entreprise (LAN) et sans fil (WLAN), les concepts de découpage en réseaux virtuels (VLAN - Virtual Local Area Network) permettent d'isoler logiquement les flux de communication de différents services (par exemple, séparer physiquement et logiquement le réseau des invités du réseau contenant les serveurs de comptabilité) sur une même infrastructure matérielle de commutateurs.

## Comparaisons

La comparaison entre le modèle OSI et le modèle TCP/IP réside dans leur approche théorique ou pratique. Le modèle OSI est un modèle conceptuel théorique strict à 7 couches utilisé principalement pour l'enseignement et la normalisation des protocoles. Le modèle TCP/IP est une suite pragmatique et concrète à 4 couches réellement implémentée dans les piles réseaux des systèmes d'exploitation pour faire fonctionner Internet.

La comparaison entre TCP et UDP porte sur la fiabilité contre la vitesse. Le protocole TCP privilégie l'exactitude absolue des données transférées grâce à des contrôles de séquencement, de déduplication et de réémission des paquets perdus au prix d'un surcoût de latence et d'en-tête réseau. UDP privilégie la vitesse brute et la faible latence en transmettant les données sans établir de connexion préalable ni vérifier la réception, acceptant la perte ponctuelle de paquets au profit du temps réel.

## Questions fréquentes

### À quoi sert le masque de sous-réseau (Subnet Mask) en réseau IP ?
Le masque de sous-réseau est une valeur binaire de 32 bits qui permet à un équipement réseau de distinguer, dans une adresse IP, la partie identifiant le réseau (Network ID) de la partie identifiant la machine hôte spécifique (Host ID). En effectuant une opération logique ET (AND) entre l'adresse IP et le masque de sous-réseau, l'équipement détermine si l'adresse de destination se trouve sur le même réseau local ou s'il doit envoyer le paquet au routeur de passerelle par défaut.

### Quelle est la différence entre un commutateur (Switch) et un routeur (Router) ?
Un commutateur (Switch) fonctionne au niveau de la couche 2 (Liaison de données) du modèle OSI. Il interconnecte des équipements au sein d'un même réseau local (LAN) en commutant des trames Ethernet basées sur les adresses physiques MAC des cartes réseau. Un routeur (Router) fonctionne au niveau de la couche 3 (Réseau) du modèle OSI. Il interconnecte des réseaux distincts (par exemple, relier un réseau local d'entreprise au réseau Internet) en routant des paquets basés sur les adresses logiques IP.

## Conclusion

Les réseaux informatiques s'appuient sur une pile standardisée de protocoles et sur l'encapsulation progressive des données pour assurer l'interconnexion mondiale des équipements. De l'adressage IP au système DNS, en passant par le routage et les protocoles de transport TCP/UDP, chaque composant garantit le transport fluide, ciblé et sécurisé des flux d'information.