import vecteursAffinites as va
import random
EPSILON = 0.05
STUDENT = "elevebf12"

def normalization(vecteur:dict):
    """ Fonction utilisée pour normaliser les vecteurs """
    # minv = min(vecteur.values())
    maxv = abs(max(vecteur.values()))
    for key in vecteur:
        # vecteur[key] = (vecteur[key] - minv)/(maxv-minv)
        vecteur[key] = vecteur[key]/maxv # entre -1 et 1

def recommendation(student,epsilon) -> str:
    """ Algorithme de recommendation de la partie 2, étape 3 """
    vecteurHexad:dict
    vecteurMotiv:dict
    vecteurHexad, vecteurMotiv = va.vecteurs(student,epsilon)
    # vecteurHexad
    # On regarde si le premier élément dans chaque vecteur
    if [*vecteurHexad.keys()][0] == [*vecteurMotiv.keys()][0]:
        return [*vecteurHexad.keys()][0]
    # On normalise les valeurs
    normalization(vecteurHexad)
    normalization(vecteurMotiv)
    maxv = 0
    maxLabel = ""
    for key in vecteurHexad:
        tmp = vecteurHexad[key] + vecteurMotiv[key]
        if (tmp > maxv) or \
            (tmp == maxv and random.random() < 0.5):
            maxv = tmp
            maxLabel = key
    return maxLabel
    
def recommendation2(student,epsilon) -> str:
    """ Autre procédé de recommendation (cf partie 2, étape 4)"""
    # En fonction du classe dans les vecteurs
    vecteurHexad:dict
    vecteurMotiv:dict
    vecteurHexad, vecteurMotiv = va.vecteurs(student,epsilon)
    rank = vecteurHexad.copy()
    for r in rank.keys():
        rank[r] = 0
    
    hexad = [*vecteurHexad.keys()]
    motiv = [*vecteurMotiv.keys()]
    size = len(hexad)
    for p in range(size):
        rank[hexad[p]] += size - p
        rank[motiv[p]] += size - p
    
    return max(rank, key=rank.get)

if __name__ == "__main__":
    reco = recommendation(STUDENT,EPSILON)
    print(f"Recommendation d'élément de jeu pour {STUDENT} : {reco}")
    reco = recommendation2(STUDENT,EPSILON)
    print(f"Recommendation2 d'élément de jeu pour {STUDENT} : {reco}")