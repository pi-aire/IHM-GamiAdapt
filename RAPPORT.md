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

Nous allons considérer les matrices ./Hexad/avatarPathCoefs ( ci-dessous *Matrice 1*) et ./Hexad/avatarpVals (ci-dessous *Matrice 2*). La matrice pVals permet de relativiser les informations issues de la première. 
Nous sommes donc dans le cadre de joueurs qui ont eu à leur disposition l'élément avatar. 
On constate pour la variation de la motivation intrinsèque, il n'est pas possible de déterminer quelque chose de significatif puisque dans la matrice 2, les valeurs de la ligne MIVar sont toutes supérieur à 0,1. En revanche, pour la motivation extrinsèque, nous constatons que des données sont exploitables. On constate par exemple, que la caractéristique "player" a eu une influence de près de 50% avec une fiabilité en la valeur assez haute (0,003). Avec une précision plus faible on peut constater que pour le profil "socialiser" cela a eu une influence négative sur la ME. Les profils "achiever", "freeSpirit", "disruptor" et "philantropist" ont une fiabilité trop faible pour pouvoir garder des informations. Pour la variation de l'amotivation, on ne peut se concentrer uniquement sur le socialiser qui provoque une variation de près de 30%. 

On constate que la fiabilité augmente pour les valeurs très franches, en revanche quand la variation est proche de 0, la fiabilité est faible.

### Etape 3 : Recommendations à partir des matrices PLS

Notre code est disponible dans le fichier [code/vecteursAffinites.py](https://github.com/pi-aire/IHM-GamiAdapt/blob/master/code/vecteursAffinites.py). A l'intérieur du fichier nous avons défini une variable globale qui permet de choisir l'étudiant souhaité. Pour calculer les motivations initiales nous avons pris le partie de simplement sommer les composantes caractéristiques de chacune des motivations. *Exemple: Motivation Intrinsèque Initiale = micoI + miacI + mistI*

Avant de chercher à déterminer le profil, nous avons pris la décision de réaliser une étape de pré-traitement afin de remplacer par 0 les valeurs avec une incertitude trop élevée. Au cours de notre exécution, nous avons fixé ce seuil à 0.05. A nouveau, nous avons déclaré une variable globale `EPSILON` afin de pouvoir paramétrer cela aisément.

Pour déterminer les vecteurs, nous avons décidé de ne pas accorder plus d'importance à l'une des deux motivations. Dans la fonction `strategy`, nous sommons la motivation intrinsèque et extrinsèque en déduisant l'amotivation. De cette façon, on s'assure que la stratégie se concentrera sur la motivation la plus élevée.

Il est possible que le vecteur soit composé uniquement de 0 et de variable inférieur à 0. Cela signifie que nous savons que certains éléments ont un effet négatif et d'autre un effet inconnu. C'est au programmeur de déterminer si il prend des risques en donnant une valeur égale à 0 car elle avait beaucoup d'incertitude ou de prendre la valeur négative la plus grande afin de limiter les pertes.

## Deuxième partie : Algorithme d'adaptation

### Etape 1 : Réflexion à partir d'exemples

Lors de notre étape de réflexion nous nous sommes concentrés sur quatre individus, elevebf12, eleveig14, elevekg10 et elevelf04. Nous avons veiller à choisir deux individus de sexe masculin et deux individus de sexe féminin. Ainsi nous espérons nous protéger d'un éventuel biais qui aurait pu être apporter par le sexe des individus.

Nous avons isolé les cas suivants :

* Cas 1 : Les vecteurs sont les mêmes. Nous choisissons donc le premier élément.
* Cas 2 : Le premier élément des deux vecteurs est le même. Nous choisissons donc le premier élément.
* Cas 3 : Les vecteurs sont inversés. (Le premier élément de l'un est le dernier élément de l'autre et ainsi de suite). La solution n'est pas évidente.
* Cas 4 : Les vecteurs semblent mélangé aléatoirement et aucun élément ne sautent aux yeux. La solution n'est pas évidente.
* Cas 5 : Toutes les valeurs sont égales à 0 ou négative. La solution n'est pas évidente.

Nous avons pris la décision de normaliser les valeurs à l'intérieur des vecteurs. Nous avons affiché les vecteurs de chacun des individus et nous avons constaté que le vecteur de motivation contenait des valeurs positives très élevées en comparaisons au valeur du vecteur du profil Hexad pour la même position au sein du vecteur. Il nous semble donc incongru de comparer ses valeurs entre elles et la normalisation nous semble la meilleure option afin de permettre une comparaison plus neutre.

### Etape 2 : Explication de la stratégie en pseudo-code

```
Titre: Recommendation d'un élément de jeu pour un élève donné
Pré-condition: Les vecteurs sont triés par ordre décroissant, 
    mesure la même taille et contiennent les labels de chacune des valeurs.
Entrée: Vecteurs d'affinités vecteurMotiv (pour la motivation) 
    et vecteurHexad (pour le profil Hexad).
Sortie: Élément recommandé
Traitement:
    vecteurMotiv ← Normalisation(vecteurMotiv)
    vecteurHexad ← Normalisation(vecteurHexad
    Si PremierLabel(vecteurMotiv) = PremierLabel(vecteurHexad) alors 
        Retourner PremierLabel(vecteurMotiv)
    Fin du Si
    max ← 0
    maxLabel ← Null
    Pour chaque label contenu dans vecteurMotiv faire:
        temporaire ← vecteurMotiv[label] + vecteurHexad[label]
        Si (temporaire > max) ou
           (temporaire = max et Aléatoire([0,1]) < 0.5)
        Alors
            max = temporaire
            maxLabel = label
        Fin du Si
    Fin du Pour
    Retourner maxLabel
Fin du traitement
```

### Etape 3 : Ecriture de l'algorithme en Python

Notre code est disponible dans le fichier [code/recommendation.py](https://github.com/pi-aire/IHM-GamiAdapt/blob/master/code/recommendation.py). Il s'occupe d'appeler le fichier de la première partie afin de générer les vecteurs d'affinités et de déterminer quel est l'élément de jeu le plus intéressant pour l'étudiant passé en paramètre. Il est important de glisser un  epsilon en paramètre afin de déterminer la précision souhaitée.

### Etape 4 : Evaluation de la pertinence

Notre réponse



/// Bloc note
approche sur la hexa
approche sur la reco motivation
approche combiné

bien justifier la stratégie

pseudo code
python


Que faire si les deux reco ne sont pas bonne
 Comment faire un compromis entre deux recommendation
 faire un 