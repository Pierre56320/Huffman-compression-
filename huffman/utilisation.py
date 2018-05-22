import huffman

fichier = "test.txt"

def compress_file(fichier_entree, fichier_sortie="test.bin"):
    with open(fichier, 'r', encoding='utf_8') as fent, open(fichier_sortie, 'wb') as fsort:
        contenu = fent.read()
        code, arbre = huffman.compresser(contenu)
        print(code)
        fsort.write(code)
        fent.close()
        fsort.close()
    return

compress_file(fichier)



