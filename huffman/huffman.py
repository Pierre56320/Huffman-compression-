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
        return (regime_Arbre(reste[0]), regime_Arbre(reste[1]))

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

def encodage(chaine, codes):
    print("chaine : ", chaine)
    print("codes : ", codes)
    code_binaire = codes
    chaine_binaire = ''
    for c in chaine:
        chaine_binaire = chaine_binaire + code_binaire[c]
    return bin(int(chaine_binaire,2))

def decodage(codes, code):
    chaine = ''
    i = ''
    if code:
        i += next([bits for bits in code])
        chaine = codes[str(i)] + decodage(codes, code[len(str(i)):])
    return chaine

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

if __name__ == "__main__":
    chaine = "BONJOUR TOUT LE MONDE"
    arbre = trouver_Codes(cree_arbre(occurrence(chaine)))
    print(arbre)
    print(encodage(chaine,arbre))