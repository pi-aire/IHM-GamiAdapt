import numpy as np
from numpy.core.fromnumeric import mean
import pandas
from pandas.core.frame import DataFrame
import warnings
warnings.filterwarnings('ignore')

EPSILON = 0.1
STUDENT = ["elevebf12","eleveig14","elevekg10","elevelf04"]
PROFILE = ["achiever","player","socialiser","freeSpirit","disruptor","philanthropist"]
MOTIV = ["MI","ME","amotI"]

def preprocess(pcs:DataFrame, pvs:DataFrame, epsilon) -> DataFrame:
    """ Les coeficients avec un p value >= epsilon sont mis à zéro
        cela supprime leurs influences
    Args:
        pcs ([DataFrame]): matrice pathCoe
        pvs ([DataFrame]): matrice pVals
        epsilon ([float]): epsilon
    Returns:
        [DataFrame]: Avec les valeurs dont l'incertitude est trop grandeà 
    """
    # On supprime les labels sur la première ligne/colomne
    for i in range(pcs.shape[0]):
        for j in range(pcs.shape[1]):
            if pvs.iloc[i,j] >= epsilon: 
                pcs.iloc[i,j] = np.float64()        
    return pcs

# def fusion(matrice, student,columns):
#     MIVar = []
#     MEVar = []
#     amotVar = []
#     for column in columns:
#         MIVar.append(matrice.loc["MIVar",column] * student[column].iloc[0])
#         MEVar.append(matrice.loc["MEVar",column] * student[column].iloc[0])
#         amotVar.append(matrice.loc["amotVar",column] * student[column].iloc[0])
#     vect = [sum(MIVar),sum(MEVar),sum(amotVar)]
#     return vect

def strategy(vecteur:DataFrame) -> float:
    """ Calcule une valeur en fonction du vecteur donné en paramètre
        Formule MI + ME - amotI
        On peut soustraire amotI car amotI est positif
    Args:
        vecteur ([type]): `len(vecteur)= 3`, contenants (MIVar,MEVar,amotVar) d'un élément de jeu d'un joueur

    Returns:
        float: valeur pour un type d'élément de jeu
    """
    vecteur = vecteur.squeeze()
    return vecteur.iloc[0] + vecteur.iloc[1] - vecteur.iloc[2] 
    # return vecteur[0] + vecteur[1] - vecteur[2]

def vecteurs(studentID,epsilon) -> tuple:
    """Retours les vecteurs d'affinités du profile heaxad et motivation
        d'un étudiant
    Args:
        studentID (str): id de l'étudiant
        epsilon (float): niveau d'incertitude maximum
    """
    # profile = ["achiever","player","socialiser","freeSpirit","disruptor","philanthropist"]
    # motiv = ["MI","ME","amotI"]
    
    userStats = pandas.read_csv("../R Code/userStats.csv",sep=";")
    student = userStats.loc[userStats["User"] == studentID]
    # Calculs des motivations innitiales
    student["MI"] = student["micoI"].iloc[0] + student[" miacI"].iloc[0] + student[" mistI"].iloc[0]
    student["ME"] = student[" meidI"].iloc[0] + student[" meinI"].iloc[0] + student[" mereI"].iloc[0]
    student["amotI"] = student[" amotI"]
    
    student = student[PROFILE+MOTIV]
    # Chargement des matrices PLS
    hexads = dict()
    motivations = dict()
    for element in ["avatar","badges","progress","ranking","score","timer"]:
        pathCoefsH = pandas.read_csv("../R Code/R Code/PLS/Hexad/"+ element +"PathCoefs.csv",sep=";",header=0,index_col=0)
        pValsH = pandas.read_csv("../R Code/R Code/PLS/Hexad/"+ element +"pVals.csv",sep=";",header=0,index_col=0)
        pathCoefsM = pandas.read_csv("../R Code/R Code/PLS/Motivation/"+ element +"PathCoefs.csv",sep=";",header=0,index_col=0)
        pValsM = pandas.read_csv("../R Code/R Code/PLS/Motivation/"+ element +"pVals.csv",sep=";",header=0,index_col=0)
        hexads[element] = preprocess(pathCoefsH,pValsH,epsilon)
        motivations[element] = preprocess(pathCoefsM,pValsM,epsilon)
    # print(hexads["avatar"])
    
    # multiplication de matrice pcs après preporcess et le profile utilisateur
    for element in ["avatar","badges","progress","ranking","score","timer"]:
        hexads[element] = hexads[element].dot(student[PROFILE].T)
        # hexads[element] = fusion(hexads[element],student,PROFILE)
        hexads[element] = strategy(hexads[element])
        motivations[element] = motivations[element].dot(student[MOTIV].T)
        # motivations[element] = fusion(motivations[element],student,MOTIV)
        motivations[element] = strategy(motivations[element])
    
    #On réalise le classement
    hexads = {key: value for key, value in sorted(hexads.items(), key=lambda item: -item[1])}   
    motivations = {key: value for key, value in sorted(motivations.items(), key=lambda item: -item[1])}   
    
    if __name__ == "__main__":
        print(student)
        print(f"\nVecteur d'affinité de {studentID} \n  pour son profil Hexad :\n   {hexads}")
        print(f"  pour son profil Motivation :\n   {motivations}\n")
    return (hexads, motivations)

if __name__ == "__main__":
    # for id in STUDENT:
    #     vecteurs(id,EPSILON)
    vecteurs(STUDENT[0],EPSILON)