from datetime import date

from numpy.lib.function_base import median
from scipy import stats
import recommendation as reco
from datetime import datetime, timezone
import pandas
import numpy as np

INFOS = ["Time","CorrectCount","FullyCompletedLessonCount","MiVar","MeVar"," amotVar"]
EPSILON = 0.05

def toSecond(date):
    dt = datetime.strptime(date, "%H:%M:%S")
    return (dt.hour * 3600) + (dt.minute * 60) + dt.second
    
def evaluate():
    """ Fonction qui réalise l'évaluation """
    # userStats = pandas.read_csv("./R Code/userStats.csv",sep=";")
    userStats = pandas.read_csv("../R Code/userStats.csv",sep=";")

    userStats["Time"] = userStats["Time"].apply(toSecond) # On converti le temps en seconde 
    userStats["MiVar"] = userStats[[" micoVar", " miacVar", " mistVar"]].sum(axis=1)
    userStats["MeVar"] = userStats[[" meidVar", " meinVar", " mereVar"]].sum(axis=1)
    
    # Recommendation
    students = userStats["User"]
    recommendations = []
    print("L'exécution du programme peut prendre un peu de temps.")
    for student in students:
        recommendations.append(reco.recommendation(student,EPSILON))
    userStats["Recomendation"] = recommendations
    # On regarde si la recommendation est la même que dans la colonne "GameElement"
    userStats["Adapted"] = userStats["Recomendation"] == userStats["GameElement"]
    
    #On réparti les groupes
    # Groupe adapté
    groupeAdapted = userStats.loc[userStats["Adapted"]]
    # Groupe non adapté
    groupeNotAdapted = userStats.loc[userStats["Adapted"] == False]
    
    print(f"Nombre de recommendations correspondantes {groupeAdapted.shape[0]}")
    print(f"Nombre de recommendations différente {groupeNotAdapted.shape[0]}")
    
    del groupeAdapted["Adapted"]
    del groupeNotAdapted["Adapted"]
    
    # On calcule les t-tests value
    for column in INFOS:
        print(f"T-test variable : {column}")
        print(stats.ttest_ind(groupeAdapted[column],groupeNotAdapted[column]))
    
if __name__ == "__main__":
    evaluate()