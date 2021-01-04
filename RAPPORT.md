# TP Gamification adaptative 

### BRUNEAU Richard - VASLIN Pierre P1914433

pathCoefs = influence
pVals = p.values = marge d'erreur

MI  = motivation intrinsèque      
MIVar = variation motivation intrinsèque (variation sur les 10 séances)
ME = motivation extrinsèque 
MEVar = variation motivation extrinsèque (variation sur les 10 séances)
amotI = la non motivation
amotVar = variation la non motivation (variation sur les 10 séances)

PLS/Motivation -> Formulaire motivation math formulaire AMS
PLS/Hexad -> profil de joueur HEXAD



## Première partie : Recommandations à partir de profils

### Etape 2 : Analyses PLS (PLS Path modeling)

*Décrivez/Commentez deux des matrices de résultats de l'analyse PLS*

Nous allons considérer les matrices ./Hexad/avatarPathCoefs ( ci-dessous *Matrice 1*) et /Hexad/avatarpVals (ci-dessous *Matrice 2*). La matrice pVals permet de relativiser les informations issues de la première. 
Nous sommes donc dans le cadre de joueurs qui ont eu à leur disposition l'élément avatar. 
On constate pour la variation de la motivation intrinsèque, il n'est pas possible de déterminer quelque chose de signification puisque dans la matrice 2, les valeurs de la ligne MIVar sont toutes supérieur à 0,1. En revanche, pour la motivation extrinsèque, nous constatons que des données sont exploitables. On constate par exemple, que la caractéristique "player" a eu une influence de près de 50% avec une fiabilité en la valeur assez haute (0,003). Avec une précision plus faible on peut constater que le profil "socialiser" a une influence négative sur la ME. Les profils "freeSpirit", "disruptor" et "philantropist" ont quand a eux une fiabilité faible. Pour la variation de l'amotivation, on ne peut se concentrer uniquement sur le socialiser qui provoque une variation de près de 30%. 

On constate que la fiabilité augmente pour les valeurs très franches, en revanche quand la variation est proche de 0, la fiabilité est faible. 

### Etape 3 : Recommendations à partir des matrices PLS

Lien vers le code 

Justifications

## Deuxième partie : Algorithme d'adaptation 

### Etape 1 : Réflexion à partir d'exemples 

Notre réponse

### Etape 2 : Explication de la stratégie en pseudo-code 

Notre réponse

### Etape 3 : Ecriture de l'algorithme en Python

Lien vers le code

### Etape 4 : Evaluation de la pertinence 

Notre réponse


approche sur la hexa
approche sur la reco motivation
approche combiné

bien justifier la stratégie

pseudo code
python


Que faire si les deux reco ne sont pas bonne
 Comment faire un compromis entre deux recommendation
 faire un 