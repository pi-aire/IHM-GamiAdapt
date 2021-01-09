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
On constate pour la variation de la motivation intrinsèque, il n'est pas possible de déterminer quelque chose de significatif puisque dans la matrice 2, les valeurs de la ligne MIVar sont toutes supérieur à 0,1. En revanche, pour la motivation extrinsèque, nous constatons que des données sont exploitables. On constate par exemple, que la caractéristique "player" a eu une influence de près de 50% avec une fiabilité en la valeur assez haute (0,003). Avec une précision plus faible on peut constater que pour le profil "socialiser" cela a eu une influence négative sur la ME. Les profils "achiever", "freeSpirit", "disruptor" et "philantropist" ont une fiabilité trop faible pour pouvoir garder des informations. Pour la variation de l'amotivation, on ne peut se concentrer uniquement sur le socialiser qui provoque une variation de près de 30%. 

On constate que la fiabilité augmente pour les valeurs très franches, en revanche quand la variation est proche de 0, la fiabilité est faible.

### Etape 3 : Recommendations à partir des matrices PLS

Notre code est disponible dans le fichier [code/partie1.py](https://github.com/pi-aire/IHM-GamiAdapt/blob/master/code/partie1.py). A l'intérieur du fichier nous avons défini une variable globale qui permet de choisir l'étudiant souhaité. Pour calculer les motivations initiales nous avons pris le partie de simplement sommer les composantes caractéristiques de chacune des motivations. *Exemple: Motivation Intrinsèque Initiale = micoI + miacI + mistI*

Avant de chercher à déterminer le profil, nous avons pris la décision de réaliser une étape de pré-traitement afin de remplacer par 0 les valeurs avec une incertitude trop élevée. Au cours de notre exécution, nous avons fixé ce seuil à 0.1. A nouveau, nous avons déclaré une variable globale `EPSILON` afin de pouvoir paramétrer cela aisément.

Pour déterminer les vecteurs, nous avons décidé de ne pas accorder plus d'importance à l'une des deux motivations. Dans la fonction `strategy`, nous sommons la motivation intrinsèque et extrinsèque en déduisant l'amotivation. De cette façon, on s'assure que la stratégie se concentrera sur la motivation la plus élevée.

TODO: Parler de la prise de risque quand les données sont négative ou égale à 0

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