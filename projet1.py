from math import *

def norme_vecteur(V):
    """
    calcul de la norme d'un vecteur plan
    parametre: "V" : liste de 2 elements contenant les coordonnees selon x et y de V
    Sortie : "n" : norme du vectur v
    """
    n= abs (sqrt(V[0]**2+V[1]**2))
    return n

def vecteur_CA(O01):
    """
    calcul du vecteur CA en fonction de l'angle theta01
    parametre: "O01": la valeur de l'angle theta01 en degre
    sortie: "CA" : une liste retournant les composantes selon x0, et y0 du vecteur CA
    """
    x= (-a -c*sin(O01*pi/180))
    y= (-b + c*cos(O01*pi/180))
    CA= [x,y]
    return CA

def angle_alpha(CA):
    """
    calcul de l'angle alpha a partir du vecteur CA=x.x0+y.y0
    parametre : "CA": une liste retournant les composantes selon x0, et y0 du vecteur CA
    sortie: "alpha" : la valeur de l'angle alpha en degre
    """
    alpha= acos (CA[1]/(norme_vecteur(CA)))
    alpha=180*alpha/pi
    return alpha

def f1(O01,O03,e):
    """
    fonction dont le but est de preciser la valeur de la loi d'entree sortie de la chaine 1
    parametres : "O01" : valeur de l'angle theta01 en radiants
                "O03" : valeur de l'angle theta03 en radiants
                "e" : longueur e, qui correspond a la longueur BC
    Sortie : "loi1" : valeur de la loi d'entree sortie 1
    """
    a=200
    b=100
    c=25
    d=100
    f= (c*sin(O01)-e*sin(O03)+a)**2+(-c*cos(O01)+e*cos(O03)+b)**2-d**2
    return f

def zero_par_secante(O0,O1,O01,epsilon,f1,e):
    """
    fonction dont le but est de trouver la valeur ou la fonction f1 s'annule
    parametres :"O0":borne inferieure de la plage des solutions en radiants
               "O1":borne superieure de la plage des solutions en radiants
               "O01":valeur de l'angle theta01 en radiants
               "epsilon":valeur limite avant que le programme ne rentre plus dans la boucle
               "f1":fonction calculant la valeur de la loi d'entree sortie
               "ecart":ecart entre les deux occurences de la fonction
               "e": longueur e, qui correspond à la longueur BC
    sortie:    "X": une bonne approximation d'une valeur telle que f1 s'annule
    """
    ecart = 1
    while (ecart >= epsilon):
        m=f1(O01,O1,e)
        n=f1(O01,O0,e)
        X=O1-((O1-O0)/(m-n))*m
        ecart=abs(X-O1)
        O0=O1
        O1=X
    return X
def calcul_amplitude():
    """
    fonction calculant l'amplitude de la chaine 1 selon differentes valeurs de e
    sans parametres ni sorties.
    """
    liste_valeurs_e=[150,160,170,180,190,200]
    for i in range(len(liste_valeurs_e)):
        e=liste_valeurs_e[i]
        L=[]
        for k in range(360):
            O01=k*2*pi/360
            L.append(zero_par_secante(0,alpha*pi/180,O01,10**-6,f1,e))    #Mélanie #les tetha0 et tetha1 ils sont pas en fonction de alpha ??
        maximum=max(L)                                                             #du coup j'ai mis ça, ça change pas pour celui là mais la
        minimum=min(L)                                                             #chaine deux ça change tout(on avait mit 0 et pi avant)
        debattement=maximum-minimum
        debattement=debattement*180/pi          #Mélanie          #ici je me suis dit que le debattement trouve etait en radian, pas en degre
        print("le debattement angulaire de e=",liste_valeurs_e[i],"est:",debattement)   #mais je suis pas sur que ça soit bon

#programme principal

x=1
y=1
O01=25
O03=30
e=180
V=[x,y]
a=200
b=100
c=25
d=100

##print ("la valeur de la norme du vecteur V est:",norme_vecteur(V))

##print ("les coordonnees du vecteur CA sont:",vecteur_CA(O01))
CA= vecteur_CA(O01)                                         #nous avons besoin d'avoir les composantes de CA dans la suite
print ("la valeur de l'angle alpha est:",angle_alpha(CA))
alpha=angle_alpha(CA)                                       #nous calculons la valeur de l'angle alpha qui va nous servir par la suite
##print ("la valeur de f1 est:",f1(O01,O03,e))

print(zero_par_secante(0,pi,pi/2,10**-8,f1,180))

print(calcul_amplitude())   #on cherche a trouver un debattement valant 15 degres, avec une erreur de 0.5 degres et en deduire la valeur de e
                            #correspondante.