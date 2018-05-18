import huffman
class h_objet():
    def __init__(self,mot):
        self.hobjet = mot

    def compresser(self):
        arbre = huffman.cree_arbre(huffman.occurrence(self.hobjet))
        self.hobjet = (arbre, huffman.encodage(huffman.trouver_Codes(arbre),self.hobjet))

    def decompresser(self):
        self.hobjet = huffman.decodage(huffman.trouver_Codes(self.hobjet[0]),self.hobjet[1])
