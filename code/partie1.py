import numpy
import pandas

EPSILON = 0.05

def preprocess(pcs, pvs, epsilon):
    """les coeficients avec un p value >= epsilon sont mis à zéro
        cela supprime leurs influences
    Args:
        pcs ([DataFrame]): matrice pathCoe
        pvs ([DataFrame]): matrice pVals
        epsilon ([float]): epsilon
    Returns:
        [DataFrame]: [description]
    """
    if pcs.shape != pvs.shape:
        exit(-1)
    for i in range(pcs.shape[0]):
        for j in range(pcs.shape[1]):
            if pvs.iloc[i,j] >= epsilon: 
                pcs.iloc[i,j] = 0.0
    return pcs

def strategy(vecteur) -> float:
    """Calcul une valeur en fonction du vecteur donné en paramètre

    Args:
        vecteur ([type]): `len(vecteur)= 3`, contenants (MIVar,MEVar,amotVar) d'un élément de jeu d'un joueur

    Returns:
        float: valeur pour un type d'élément de jeu
    """
    pass

def main() -> None:
    feels = ["achiever","player","socialiser","freeSpirit","disruptor","philanthropist"]
    
    userStats = pandas.read_csv("../R Code/userStats.csv",sep=";")
    student = userStats.loc[userStats["User"] == "elevebf12"]
    student = student[feels]
    print(student)
    
    # Chargement des matrices PLS
    hexads = dict()
    motivations = dict()
    for element in ["avatar","badges","progress","ranking","score","timer"]:
        hexads[element] = dict()
        motivations[element] = dict()
        for mat in ["PathCoefs","pVals"]: # a modifié car prépocessing
            hexads[element][mat] = pandas.read_csv("../R Code/R Code/PLS/Hexad/"+ element+mat +".csv",sep=";")
            motivations[element][mat] = pandas.read_csv("../R Code/R Code/PLS/Motivation/"+ element+mat +".csv",sep=";")
    # print(hexads)
    ## multiplication de matrice pcs après preporcess et tranpot de student, 
    # avec ça on obtient un vecteur (MIVar,MEVar,amotVar), 
    # aprés définir (strtégie) une valeur avec les trois valeurs puis avec la valeur obtenu la compare au valeur des autre type (ex: badges, progress, etc) et on les classes
    # Creation du vecteur d'affinité pour son profil Hexad
    
    # Creation du vecteur d'affinité pour son profil de motivation


# vecteur
# [valueAvatar, valueBadge, etc...]

if __name__ == "__main__":
    main()