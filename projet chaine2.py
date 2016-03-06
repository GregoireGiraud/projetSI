from math import *
def norme_vecteur(V):
    """
    calcul de la norme d'un vecteur plan
    parametre: "V" : liste de 2 elements contenant les coordonnees selon x et y de V
    Sortie:   "n" : norme du vectur v
    """
    n= abs (sqrt(V[0]**2+V[1]**2))
    return n

def vecteur_GE(O34):
    """
    calcul du vecteur GE en fonction de l'angle theta01
    paramètre: "O34": la valeur de l'angle theta34 en degre
    sortie:    "GE" : une liste retournant les composantes selon z3, et x3 du vecteur GE
    """
    z3=i-f*sin(O34)*180/pi
    x3=j+f*cos(O34)*180/pi
    GE= [z3,x3]
    return GE

def angle_beta(GE):
    """
    calcul de l'angle beta à partir du vecteur GE
    paramètre: "GE": une liste retournant les composantes selon z3, et x3 du vecteur GE
    sortie:    "beta" : la valeur de l'angle beta en degre
    """
    beta= acos (GE[0]/(norme_vecteur(GE)))
    return 180*beta/pi


#fonction f2
def f2(O34,O36,j):
    """
    fonction dont le but est de preciser la valeur de la loi d'entree sortie de la chaine 1
    parametres:"O34" : valeur de l'angle theta34 en radiants
              "O36" : valeur de l'angle theta36 en radiants
              "j" : longueur j, qui correspond a la composante en x3 de GD
    Sortie:   "loi2" : valeur de la loi d'entrée sortie2
    """
    loi2=(i-f*sin(O34)-h*cos(O36))**2+(j+f*cos(O34)-h*sin(O36))**2-g**2
    return loi2
def zero_par_secante(O0,O1,O34,epsilon,f2,j):
    """
    fonction dont le but est de trouver la valeur ou la fonction f1 s'annule
    parametres:"O0":borne inferieure de la plage des solutions en radiants
               "O1":borne superieure de la plage des solutions en radiants
               "O34":valeur de l'angle theta34 en radiants
               "epsilon":valeur limite avant que le programme ne rentre plus dans la boucle
               "f2":fonction calculant la valeur de la loi d'entree d'entree
               "j": longueur j, qui correspond à la composante en x3 de GD
    sortie:    "X": une bonne approximation d'une valeur telle que f2 s'annule
    """
    ecart=1
    while (ecart>=epsilon):
        m=f2(O34,O1,j)
        n=f2(O34,O0,j)
        X=O1-(((O1-O0)/(m-n))*m)
        ecart=abs(X-O1)
        O0=O1
        O1=X
    return X

def calcul_amplitude():
    """
    fonction calculant l'amplitude de la chaine 1 selon differentes valeurs de j
    sans parametres ni sorties.
    """
    liste_valeurs_j=[40,41,42,43,44,45]
    for i in range(len(liste_valeurs_j)):
        j=liste_valeurs_j[i]
        L=[]
        for k in range(360):
            O34=k*pi/180
            L.append(zero_par_secante(beta*pi/180,pi,O34,10**-6,f2,j))         #Mélanie #même remarque qu'a la chaine 1, beta sert à ça je
        maximum=max(L)                                                                  #crois. si on mettait 0,pi on avait des valeurs
        minimum=min(L)                                                                  #aberrantes
        debattement=maximum-minimum
        debattement=debattement*180/pi
        print("le debattement angulaire de j=",liste_valeurs_j[i],"est:",debattement)

#programme principal
O36=50
epsilon=10**-8
j=40
O34=22
f=20
g=50
h=25
i=25

##print ("les coordonnees du vecteur GE sont:",vecteur_GE(O34))
GE= vecteur_GE(O34)                                     #nous avons besoin d'avoir les composantes de GE dans la suite
##
print ("la valeur de l'angle beta est:",angle_beta(GE))
beta=angle_beta(GE)                                     #nous calculons la valeur de l'angle alpha qui va nous servir par la suite
##
##print ("la valeur de f2 est:",f2(O34,O36,j))
##
print(zero_par_secante(0,pi,pi/2,epsilon,f2,j))

print(calcul_amplitude())   #on cherche a trouver un debattement valant 105 degres à 2 degres pres et en deduire la valeur de j
                            #correspondante.