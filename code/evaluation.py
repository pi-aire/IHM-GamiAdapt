from datetime import date

from numpy.lib.function_base import median
import recommendation as reco
from datetime import datetime, timezone
import pandas
import numpy as np

AMOT = " amotVar"
MOTIVATIONSVAR = [" micoVar", " miacVar", " mistVar", " meidVar", " meinVar", " mereVar", " amotVar"]
INFOS = ["Time","CorrectCount","FullyCompletedLessonCount"]
NORMALIZE = ["Time","CorrectCount","FullyCompletedLessonCount","MotVar"]
EPSILON = 0.05
SCORE_MIN = 0.3 # Faire varier le seuil

def toSecond(date):
    dt = datetime.strptime(date, "%H:%M:%S")
    return (dt.hour * 3600) + (dt.minute * 60) + dt.second
    
def evaluate():
    userStats = pandas.read_csv("../R Code/userStats.csv",sep=";")
    # userStats = userStats.head(10)
    userStats["Time"] = userStats["Time"].apply(toSecond)
    userStats[AMOT] = userStats[AMOT] * -1
    userStats["MotVar"] = userStats[MOTIVATIONSVAR].sum(axis=1)
    
    #Normalization
    for colum in NORMALIZE:
        userStats[colum] = userStats[colum] / userStats[colum].abs().max() 

    # Score
    userStats["Score"] = userStats[NORMALIZE].sum(axis=1)
    # print(userStats["Score"])
    # Stisfaction du joueur
    # mean = userStats["Score"].mean()
    # print(median)
    userStats["Satisfied"] = userStats["Score"] > SCORE_MIN
    
    # Recommendation
    students = userStats["User"]
    recommendations = []
    print("@Richard attend le calcul peut mettre du temps 😉, le programme n'est pas planté")
    for student in students:
        recommendations.append(reco.recommendation(student,EPSILON))
    userStats["Recomendation"] = recommendations
    
    # On regarde si la recommendation et la même que l'utilisateur à fait
    userStats["Adapted"] = userStats["Recomendation"] == userStats["GameElement"]
    # On évalue le recommendation en fonction du score
    userStats["GoodRecomendation"] = (userStats["Adapted"] & userStats["Satisfied"]) | \
        (np.logical_not(userStats["Adapted"]) & userStats["Satisfied"])
    total = userStats["GoodRecomendation"].sum()
    print(f"Nombre de bonne et potentiellement bonne recommendation: {total}/{userStats.shape[0]} \n Bonjour 🙋‍ @Richard il faut prendre le résultat avec des pincettes, regarde bien la manière de calculer les scores\n et le SCORE_MIN qui est le seuil de satisfaction")
    
    
if __name__ == "__main__":
    evaluate()