import huffman

fichier = "test.txt"

def compress_file(fichier_entree):
    with open(fichier, 'r', encoding='utf_8') as fent, open(fichier_entree[:-4]+'.bin', 'wb') as fsort:
        contenu = fent.read()
        code = huffman.compresser(contenu)
        fsort.write(code)
        fent.close()
        fsort.close()
    return

def decompress_file(fichier_entree):
    with open(fichier, 'rb') as fent, open(fichier_entree[:-4]+'.txt', 'w', encoding='utf-8') as fsort:
        contenu = fent.read()
        chaine = huffman.decompresser(contenu)
        fsort.write(chaine)
        fent.close()
        fsort.close()
    return

compress_file(fichier)



