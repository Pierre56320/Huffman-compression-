#TM-PG-VG
from bitstring import BitArray
import bson

def occurrence(chaine):
    occ = {}
    for caractere in chaine:
        occ[caractere] = chaine.count(caractere)
    return occ

def cree_arbre(occ):
    arbre = [(occ, lettre) for (lettre, occ) in occ.items()]
    arbre.sort()  # mets les occurences dans l'ordre
    while len(arbre) > 1:
        noeud1, noeud2 = arbre[0], arbre[1]
        arbre = arbre[2:]
        arbre.append((noeud1[0] + noeud2[0], (noeud1, noeud2)))
        arbre.sort(key=lambda x: x[0])
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
    return codes

def encodage(chaine, codes_binaire):
    chaine_binaire = bson.dumps(codes_binaire)
    chaine_binaire = BitArray(chaine_binaire).bin
    taille_codes_binaire = str(bin(len(chaine_binaire)))[2:]
    print(str(bin(len(chaine_binaire)))[2:])
    chaine_binaire = "1" + taille_codes_binaire + chaine_binaire
    for k in range(len(taille_codes_binaire)):
        chaine_binaire = "0" + chaine_binaire
    print(chaine_binaire)
    for c in chaine:
        chaine_binaire = chaine_binaire + codes_binaire[c]
    nb_bits_rest = len(chaine_binaire)%8
    chaine_binaire_decoupe = []
    while chaine_binaire:
        chaine_binaire_decoupe.append(chaine_binaire[:8])
        chaine_binaire = chaine_binaire[8:]
    for k in range(8 - nb_bits_rest): #On rajoute des 0 de manière a obtenir un octet
        chaine_binaire_decoupe[-1]= chaine_binaire_decoupe[-1]+'0'
    #on indique sur le dernier octet le nb de 0 a enlever
    chaine_binaire_decoupe.append(str(bin(8 - nb_bits_rest))[2:].zfill(8))
    return bytes([int(group, 2) for group in chaine_binaire_decoupe])

def decodage(mot_binaire):
    mot_decode = ''
    tampon = ''
    k = 0
    print(mot_binaire)
    mot_binaire = str(BitArray(mot_binaire).bin)
    print(mot_binaire)
    while mot_binaire[k] == "0":
        k += 1
    taille_arbre, mot_binaire = mot_binaire[k+1: k+k+1],mot_binaire[k+k+1:]
    arbre, mot_binaire = mot_binaire[:int(taille_arbre,2)], mot_binaire[int(taille_arbre,2):]
    arbre_binaire_decoupe = []
    while arbre:
        arbre_binaire_decoupe.append(arbre[:8])
        arbre = arbre[8:]
    codes = bson.loads(bytes([int(group, 2) for group in arbre_binaire_decoupe]))
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
    for k in range(10):
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
    codes_binaires = trouver_Codes(cree_arbre(occurrence(chaine)))
    return encodage(chaine,codes_binaires)

def decompresser(mot_binaire):
    return decodage(mot_binaire)


if __name__ == "__main__":
    chaine = "ceci est un test de comp gnirag  rn675Giç9"
    a = compresser(chaine)
    c= decompresser(a)
    print(c)
