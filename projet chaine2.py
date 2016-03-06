from math import *
def norme_vecteur(V):
    """
    calcul de la norme d'un vecteur plan
    paramètre: "V" : liste de 2 éléments contenant les coordonnées selon x et y de V
    Sortie : "n" : norme du vectur v
    """
    n= abs (sqrt(V[0]**2+V[1]**2))
    return n

def vecteur_GE(O34):
    """
    calcul du vecteur GE en fonction de l'angle tÃ©ta01
    paramètre: "O34": la valeur de l'angle théta34 en degré
    sortie: "GE" : une liste retournant les composantes selon z3, et x3 du vecteur GE
    """
    z3=i-f*sin(O34)*180/pi
    x3=j+f*cos(O34)*180/pi
    GE= [z3,x3]
    return GE

def angle_alpha(GE):
    """
    calcul de l'angle alpha Ã  partir du vecteur GE
    paramètre : "GE": une liste retournant les composantes selon z3, et x3 du vecteur GE
    paramÃ¨tre de sortie: "alpha" : la valeur de l'angle alpha en degré
    """
    alpha= acos (GE[1]/(norme_vecteur(GE)))
    return 180*alpha/pi


#fonction f2
def f2(O34,O36,j):
    """
    fonction dont le but est de préciser la valeur de la loi d'entrée sortie de la chaine 1
    paramètre : "O34" : valeur de l'angle théta34 en degré
                "O36" : valeur de l'angle théta36 en degré
                "j" : longueur j, qui correspond à la composante en x3 de GD
    Sortie : "loi2" : valeur de la loi d'entrée sortie2
    """
    loi2=(i-f*sin(O34*pi/180)-h*cos(O36))**2+(j+f*cos(O34*pi/180)-h*sin(O36))**2-g**2
    return loi2
def zero_par_secante(O0,O1,theta_moteur,epsilon,f2,ecart,j):        #Qu'est-ce que théta_moteur ? Préciser le but du programme et la sortie

    """
    paramètres:"O0":borne inférieure de la plage des solutions
               "O1":borne supérieure de la plage des solutions
               "theta_moteur":
               "epsilon":valeur limite avant que le programme ne rentre plus dans la boucle
               "f2":fonction calculant la valeur de la loi d'entrée d'entrée
               "ecart":ecart entre les deux occurences de la fonction
               "j": longueur j, qui correspond à la composante en x3 de GD
    sortie:    "X":
    """
    while ecart>epsilon:
        m=f2(O1,theta_moteur,j)
        n=f2(O0,theta_moteur,j)
        X=O1-(((O1-O0)/(m-n))*m)
        ecart=abs(X-O1)
        O0=O1
        O1=X
    return X
#programme principal
O0,O1=0,180
O36=50
epsilon=10**-4
j=27
O34=22
f=20
g=50
ecart=7
h=25
i=25
print ("les coordonnées du vecteur GE sont:",vecteur_GE(O34))
GE= vecteur_GE(O34)
print ("la valeur de l'angle alpha est:",angle_alpha(GE))
print ("la valeur de f2 est:",f2(O34,O36,j))
print(zero_par_secante(O0,O1,O34,epsilon,f2,ecart,j))