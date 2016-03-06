from math import *
from projet111 import *


liste_valeurs_e = [150, 160, 170, 180, 190, 200]
for i in range(len(liste_valeurs_e)):
    e = liste_valeurs_e[i]
    L = []
    for k in range(360):
        O1 = k*2*pi/360
        L.append(zero_par_secante(O0, O1, theta_moteur, epsilon, f1, ecart, e))
    max, min = max(L), min(L)
    debattement = max - min
    print("le debattement angulaire de e=", liste_valeurs_e[i], "est:", debattement)
