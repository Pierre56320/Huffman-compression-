#TM-PG-VG
#from pympler import asizeof
<<<<<<< HEAD

=======
>>>>>>> master

class huffman:
    @staticmethod
    def occurrence(chaine):
        occ = {}
        for caractere in chaine:
            occ[caractere] = chaine.count(caractere)
        return occ

    @classmethod
    def cree_arbre(cls, occ):
        arbre = [(occ, lettre) for (lettre, occ) in occ.items()]
        arbre.sort()  # mets les occurences dans l'ordre
        while len(arbre) > 1:
            noeud1, noeud2 = arbre[0], arbre[1]
            arbre = arbre[2:]
            arbre.append((noeud1[0] + noeud2[0], (noeud1, noeud2)))
            arbre.sort(key=lambda x: x[0])
        return cls.regime_Arbre(arbre[0])

    @classmethod
    def regime_Arbre(cls, arbre):
        reste = arbre[1]
        if type(reste) == str:
            return reste
        else:
            return (cls.regime_Arbre(reste[0]), cls.regime_Arbre(reste[1]))

    @staticmethod
    def trouver_Codes(arbre):
        codes = {}
        def code_courant(prefixe, noeud):
            if type(noeud) == str: #  cas d'une feuille
                codes[noeud] = prefixe
            else: #  cas d'un nœud
                code_courant(prefixe + '0', noeud[0])
                code_courant(prefixe + '1', noeud[1])

        code_courant('', arbre)
        return codes

    @staticmethod
    def encodage(arbre, chaine):
        code_binaire = dict((arbre[bits], bits) for bits in arbre)
        chaine_binaire = ''
        for c in chaine:
            chaine_binaire = chaine_binaire + code_binaire[c]
        return chaine_binaire

    @classmethod
    def decodage(cls, codes, code):
        chaine = ''
        i = ''
        if code:
            i += next([bits for bits in code])
            chaine = codes[str(i)] + cls.decodage(codes, code[len(str(i)):])
        return chaine



    @staticmethod
    def afficher_arbre(arbre, valeurs):

        affichage = []
        for k in range(10):
            affichage.append([])

        def code_courant(noeud, profondeur):
            if type(noeud) == str:  #  cas d'une feuille                
                affichage[profondeur].append(noeud)

            else: #  cas d'un nœud                
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



class h_objet():
    def __init__(self,mot):
        self.hobjet = mot

    def compresser(self):
        arbre = huffman.cree_arbre(huffman.occurrence(self.hobjet))
        self.hobjet = (arbre, huffman.encodage(huffman.trouver_Codes(arbre),self.hobjet))

    def decompresser(self):
        self.hobjet = huffman.decodage(huffman.trouver_Codes(self.hobjet[0]),self.hobjet[1])


def encodage(chaine, arbre):
    code_binaire = dict((arbre[bits], bits) for bits in arbre)
    chaine_binaire = ''                        
    for c in chaine:
        chaine_binaire = chaine_binaire + code_binaire[c]
    return chaine_binaire


if __name__ == "__main__":
    """
    suite = h_objet("ABRACADABRA")
    print(huffman.occurrence("ABRACADABRA"))
    #!!! les tailles sont fausses
    print(suite.hobjet + " non compressé de taille " + str(sys.getsizeof(suite.hobjet)) + " bytes")
    suite.compresser()
    print(str(suite.hobjet) + " compressé de taille " + str(sys.getsizeof(suite.hobjet)) + " bytes")
    """
    arbre = huffman.cree_arbre(huffman.occurrence("BONJOUR TOUT LE MONDE"))
    print(arbre)
    huffman.afficher_arbre(arbre, huffman.trouver_Codes(arbre))







