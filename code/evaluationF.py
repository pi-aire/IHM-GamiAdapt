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
    userStats = pandas.read_csv("../R Code/userStats.csv",sep=";")

    userStats["Time"] = userStats["Time"].apply(toSecond) # On converti le temps en seconde 
    userStats["MiVar"] = userStats[[" micoVar", " miacVar", " mistVar"]].sum(axis=1)
    userStats["MeVar"] = userStats[[" meidVar", " meinVar", " mereVar"]].sum(axis=1)
    
    # Recommendation
    students = userStats["User"]
    recommendations = []
    print("@Richard attend le calcul peut mettre du temps 😉, le programme n'est pas planté")
    for student in students:
        recommendations.append(reco.recommendation(student,EPSILON))
    userStats["Recomendation"] = recommendations
    
    # On regarde si la recommendation et la même que l'utilisateur à fait
    userStats["Adapted"] = userStats["Recomendation"] == userStats["GameElement"]
    
    #On constitu les groupes
    # Groupe adapté
    groupeAdapted = userStats.loc[userStats["Adapted"]]
    # Groupe non adapté
    groupeNotAdapted = userStats.loc[userStats["Adapted"] == False]
    
    print(f"Nombre de recommendation adapté {groupeAdapted.shape[0]}")
    print(f"Nombre de recommendation non adapté {groupeNotAdapted.shape[0]}")
    
    # On supprime la column qui
    del groupeAdapted["Adapted"]
    del groupeNotAdapted["Adapted"]
    
    # On calcul les t-test value
    for column in INFOS:
        print(f"T-test variable : {column}")
        print(stats.ttest_ind(groupeAdapted[column],groupeNotAdapted[column]))
    # Les valeurs montre les mauvais résultat de notre système de recommendation
    
if __name__ == "__main__":
    evaluate()