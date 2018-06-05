#TM PG VG
#Entropie
#Ces fonctions servent à calculer/observer les performances de la compression

from math import log2
import os.path 

exemple = 'abcdefghijklmp'

def symboles(chaine):
    '''Repère et range les différents symboles d'une chaine dans une liste.'''
    liste = list(chaine)
    symb = set(liste)
    symb = sorted(symb)
    return symb
    
def probabilités(chaine) :   
    '''retourne une liste de la probabilité d'apparition de chaque symbole dans
    la chaine de caractère'''                        
    probabilités = []
    symb = symboles(chaine)
    for s in symb :
        probabilités.append(chaine.count(s)/len(chaine))
    return probabilités

def entropie(chaine) :
    '''Applique la formule de l'entropie, la valeur retournée correspond au
    nombre de bit/symboles nécéssaire pour décoder correctement le fichier.
    Cela peut également désigner le nombre moyen de questions à réponse
    OUI/NON qu'il faut poser à la source pour trouver le bon symbole'''   
    prob = probabilités(chaine)
    produit = list()
    for p in prob :
        produit.append(p*log2(1/p))
    H = sum(produit)
    return H*len(chaine)

#Utilisation

def calcul_entropie(fichier_entree):
    with open(fichier_entree, 'r', encoding='utf_8') as fent :
        contenu = fent.read()
        entro = entropie(contenu)
        fent.close()
    return entro

if __name__ == "__main__" :
    print(calcul_entropie('test.txt'))
