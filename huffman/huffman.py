#TM-PG-VG
from bitstring import BitArray
import bson

def occurrence(chaine):
    """calcule le nombre d'apparences de chaque caractère dans une chaine"""
    '''
    occ = {}
    for caractere in chaine: #evite de recalculer les occurences d'un même caractère plusieurs fois (énorme gain de temps)
            occ[caractere] = chaine.count(caractere)
    return occ'''
    occ = {}
    for caractere in chaine:
        if caractere in occ:
            occ[caractere] = occ[caractere] + 1
        else:
            occ[caractere] = 1
    print("fin occ")
    return occ


def cree_arbre(chaine):
    occ = occurrence(chaine)
    arbre = [(occ, lettre) for (lettre, occ) in occ.items()]
    arbre.sort()  # mets les occurences dans l'ordre
    while len(arbre) > 1:
        noeud1, noeud2 = arbre[0], arbre[1]
        arbre = arbre[2:]
        arbre.append((noeud1[0] + noeud2[0], (noeud1, noeud2)))
        arbre.sort(key=lambda x: x[0])
    print("fin creer arbre")
    return regime_Arbre(arbre[0])

def regime_Arbre(arbre):
    reste = arbre[1]
    if type(reste) == str:
        return reste
    else:
        return regime_Arbre(reste[0]), regime_Arbre(reste[1])

def trouver_Codes(arbre):
    codes = {}
    def code_courant(prefixe, noeud):
        if type(noeud) == str:  #  cas d'une feuille
            codes[noeud] = prefixe
        else:  #  cas d'un nœud
            code_courant(prefixe + '0', noeud[0])
            code_courant(prefixe + '1', noeud[1])
    code_courant('', arbre)
    print("fin trouver codes")
    return codes

def encodage(chaine, codes_binaire):
    chaine_binaire = bson.dumps(codes_binaire)
    chaine_binaire = BitArray(chaine_binaire).bin
    taille_codes_binaire = str(bin(len(chaine_binaire)))[2:]
    chaine_binaire = "1" + taille_codes_binaire + chaine_binaire
    # print(mot_binaire)
    for k in range(len(taille_codes_binaire)):
        chaine_binaire = "0" + chaine_binaire
    for c in chaine:
        chaine_binaire = chaine_binaire + codes_binaire[c]
    nb_bits_rest = len(chaine_binaire)%8
    for k in range(8 - nb_bits_rest): #On rajoute des 0 de manière a obtenir un octet
        chaine_binaire= chaine_binaire +'0'
    #on indique sur le dernier octet le nb de 0 a enlever
    chaine_binaire = chaine_binaire + str(bin(8 - nb_bits_rest))[2:].zfill(8)
    #on sépare la chaine de caractère en liste de chaines de 8 caractères
    #on converti les octets en base 2 (0-255)
    #on converti ensuite se nombre en objet python bytes
    return bytes(int(chaine_binaire[i:i+8],2) for i in range(0,len(chaine_binaire),8))

def decodage(mot_binaire):
    mot_decode = ''
    tampon = ''
    k = 0
    mot_binaire = str(BitArray(mot_binaire).bin)
    #print(mot_binaire)
    while mot_binaire[k] == "0":
        k += 1
    taille_arbre, mot_binaire = mot_binaire[k+1: k+k+1],mot_binaire[k+k+1:]
    arbre, mot_binaire = mot_binaire[:int(taille_arbre,2)], mot_binaire[int(taille_arbre,2):]
    arbre_binaire_decoupe = []
    codes = bson.loads(bytes(int(arbre[i:i+8],2) for i in range(0,len(arbre),8)))
    mot_binaire, nb_0_sup = mot_binaire[:-8], int(mot_binaire[-8:],2)
    mot_binaire = mot_binaire[:-nb_0_sup] #On supprime les 0
    codes = {v: k for k, v in codes.items()}
    for b in mot_binaire:
        tampon = tampon+b
        if tampon in codes:
            mot_decode = mot_decode + codes[tampon]
            tampon = ''
    return mot_decode

def afficher_arbre(arbre, valeurs):
    affichage = []
    def profondeur_max(noeud):
        if type(noeud) == str:
            return 1;
        else:
            # comparer la profondeur de chaque sous-element
            profondeurG = profondeur_max(noeud[0])
            profondeurD = profondeur_max(noeud[1])
            return max(profondeurD, profondeurG)+1
    for k in range(profondeur_max(arbre)):
        affichage.append([])

    def code_courant(noeud, profondeur):
        if type(noeud) == str:  #  cas d'une feuille
            affichage[profondeur].append(noeud)

        else:  #  cas d'un nœud
            affichage[profondeur].append("#")
            code_courant(noeud[0], profondeur + 1)
            code_courant(noeud[1], profondeur + 1)
    code_courant(arbre, 0)
    for ligne in affichage:
        for caractere in ligne:
            try:
                print(caractere + ":" + valeurs[caractere], end=' ')
            except:
                print(caractere, end=' ')
        print('\n')

def compresser(chaine):
    arbre = cree_arbre(chaine)
    codes_binaires = trouver_Codes(arbre)
    return encodage(chaine,codes_binaires)

def decompresser(mot_binaire):
    return decodage(mot_binaire)


if __name__ == "__main__":
    chaine = "ceci est un test de comp gnirag  rn675Giç9"
    #arbre  = cree_arbre(chaine)
    #codes = trouver_Codes(arbre)
    #afficher_arbre(arbre,codes)

    a = compresser(chaine)
    c= decompresser(a)
    print(c)
