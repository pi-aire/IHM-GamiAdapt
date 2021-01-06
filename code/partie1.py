import numpy as np
import pandas
from pandas.core.frame import DataFrame

EPSILON = 0.1
STUDENT = "elevebf12"

def preprocess(pcs:DataFrame, pvs:DataFrame, epsilon) -> DataFrame:
    """les coeficients avec un p value >= epsilon sont mis à zéro
        cela supprime leurs influences
    Args:
        pcs ([DataFrame]): matrice pathCoe
        pvs ([DataFrame]): matrice pVals
        epsilon ([float]): epsilon
    Returns:
        [DataFrame]: [description]
    """
    # On supprime les labels sur la première ligne/colomne
    for i in range(pcs.shape[0]):
        for j in range(pcs.shape[1]):
            if pvs.iloc[i,j] >= epsilon: 
                pcs.iloc[i,j] = np.float64()        
    return pcs

def strategy(vecteur:DataFrame) -> float:
    """Calcul une valeur en fonction du vecteur donné en paramètre
        Formule MI + ME - amotI
        On peut soustraire amotI car amotI est positif
    Args:
        vecteur ([type]): `len(vecteur)= 3`, contenants (MIVar,MEVar,amotVar) d'un élément de jeu d'un joueur

    Returns:
        float: valeur pour un type d'élément de jeu
    """
    vecteur = vecteur.squeeze()
    return vecteur.iloc[0] + vecteur.iloc[1] - vecteur.iloc[2] 

def main() -> None:
    profile = ["achiever","player","socialiser","freeSpirit","disruptor","philanthropist"]
    motiv = ["MI","ME","amotI"]
    
    userStats = pandas.read_csv("../R Code/userStats.csv",sep=";")
    student = userStats.loc[userStats["User"] == STUDENT]
    # Calcul des motivations innitiales
    student["MI"] = student["micoI"].iloc[0] + student[" miacI"].iloc[0] + student[" mistI"].iloc[0]
    student["ME"] = student[" meidI"].iloc[0] + student[" meinI"].iloc[0] + student[" mereI"].iloc[0]
    student["amotI"] = student[" amotI"]
    student = student[profile+motiv]
    print(student)
    # Chargement des matrices PLS
    hexads = dict()
    motivations = dict()
    for element in ["avatar","badges","progress","ranking","score","timer"]:
        pathCoefsH = pandas.read_csv("../R Code/R Code/PLS/Hexad/"+ element +"PathCoefs.csv",sep=";",header=0,index_col=0)
        pValsH = pandas.read_csv("../R Code/R Code/PLS/Hexad/"+ element +"pVals.csv",sep=";",header=0,index_col=0)
        pathCoefsM = pandas.read_csv("../R Code/R Code/PLS/Motivation/"+ element +"PathCoefs.csv",sep=";",header=0,index_col=0)
        pValsM = pandas.read_csv("../R Code/R Code/PLS/Motivation/"+ element +"pVals.csv",sep=";",header=0,index_col=0)
        hexads[element] = preprocess(pathCoefsH,pValsH,EPSILON)
        motivations[element] = preprocess(pathCoefsM,pValsM,EPSILON)
    # print(hexads["avatar"])
    
    # multiplication de matrice pcs après preporcess et le profile utilisateur
    for element in ["avatar","badges","progress","ranking","score","timer"]:
        hexads[element] = hexads[element].dot(student[profile].T)
        hexads[element] = strategy(hexads[element])
        motivations[element] = motivations[element].dot(student[motiv].T)
        motivations[element] = strategy(motivations[element])
    
    #ON réalise le classement
    hexads = {key: value for key, value in sorted(hexads.items(), key=lambda item: -item[1])}   
    motivations = {key: value for key, value in sorted(motivations.items(), key=lambda item: -item[1])}   
    print(f"Vecteur d'affinité de {STUDENT} \n  pour son profil Hexad :\n   {hexads}")
    print(f"  pour son profil Motivation :\n   {motivations}")

if __name__ == "__main__":
    main()