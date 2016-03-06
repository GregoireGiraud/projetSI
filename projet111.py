from math import *
def norme_vecteur(V):
    """
    calcul de la norme d'un vecteur plan
    paramètre: "V" : liste de 2 éléments contenant les coordonnées selon x et y de V
    Sortie : "n" : norme du vectur v
    """
    n= abs (sqrt(V[0]**2+V[1]**2))
    return n

def vecteur_CA(O01):
    """
    calcul du vecteur CA en fonction de l'angle théta01
    paramètre: "O01": la valeur de l'angle théta01 en degré
    sortie: "CA" : une liste retournant les composantes selon x0, et y0 du vecteur CA
    """
    x= (-a -c*sin(O01*pi/180))
    y= (-b + c*cos(O01*pi/180))
    CA= [x,y]
    return CA
def angle_alpha(CA):
    """
    calcul de l'angle alpha Ã  partir du vecteur CA=x.x0+y.y0
    paramètre : "CA": une liste retournant les composantes selon x0, et y0 du vecteur CA
    sortie: "alpha" : la valeur de l'angle alpha en degré
    """
    alpha= acos (CA[1]/(norme_vecteur(CA)))
    return 180*alpha/pi
def f1(O01,O03,e):
    """
    fonction dont le but est de préciser la valeur de la loi d'entrée sortie de la chaine 1
    paramètre : "O01" : valeur de l'angle théta01 en degré
                "O03" : valeur de l'angle théta03 en degré
                "e" : longueur e, qui correspond à la longueur BC
    Sortie : "loi1" : valeur de la loi d'entrée sortie 1
    """
    loi1= (c*sin(O01*pi/180)-e*sin(O03*pi/180)+a)**2+(-c*cos(O01*pi/180)+e*cos(O03*pi/180)+b)**2-d**2
    return loi1

def zero_par_secante(O0,O1,theta_moteur,epsilon,f1,ecart,e):         #Qu'est-ce que théta_moteur ? Préciser le but du programme et la sortie
    """

    paramètres:"O0":borne inférieure de la plage des solutions
               "O1":borne supérieure de la plage des solutions
               "theta_moteur":
               "epsilon":valeur limite avant que le programme ne rentre plus dans la boucle
               "f1":fonction calculant la valeur de la loi d'entrée d'entrée
               "ecart":ecart entre les deux occurences de la fonction
               "e": longueur e, qui correspond à la longueur BC
    sortie:    "X":
    """
    while ecart>epsilon:
        m=f1(O1,theta_moteur,e)
        n=f1(O0,theta_moteur,e)
        X=O1-(((O1-O0)/(m-n))*m)
        ecart=abs(X-O1)
        O0=O1
        O1=X
    return X
#programme principal
O0=0
O1=180
epsilon= 10^-5
x=1
y= 1
O01= 25
O03= 30
e=87
ecart=3
V=[x,y]
a= 200
b=100
c=25
d=100
print ("la valeur de la norme du vecteur V est:",norme_vecteur(V))

print ("les coordonnÃ©es du vecteur CA sont:",vecteur_CA(O01))
CA= vecteur_CA(O01)
print ("la valeur de l'angle alpha est:",angle_alpha(CA))
print ("la valeur de f1 est:",f1(O01,O03,e))

zero_par_secante(O0,O1,O01,epsilon,f1,ecart,e)
