#TM-PG-VG
#from pympler import asizeof


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
    chaine_binaire = ''
    for c in chaine:
        chaine_binaire = chaine_binaire + codes_binaire[c]
    chaine_binaire_decoupe = []
    while chaine_binaire:
        chaine_binaire_decoupe.append(chaine_binaire[:8])
        chaine_binaire = chaine_binaire[8:]
    return bytes([int(group, 2) for group in chaine_binaire_decoupe])

def decodage(codes, mot_binaire):
    mot_decode = ''
    tampon = ''
    print(mot_binaire)
    return
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
    return (encodage(chaine,codes_binaires),codes_binaires)

def decompresser(mot_binaire,codes_binaires):
    return decodage(codes_binaires,mot_binaire)


if __name__ == "__main__":
    chaine = "ceci est un test de compréssion"
    a,b = compresser(chaine)
    c= decompresser(a,b)
