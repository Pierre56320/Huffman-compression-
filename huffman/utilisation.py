import huffman
import base64
from io import BytesIO

def compress_file(fichier_entree):
    with open(fichier_entree, 'r', encoding='utf_8') as fent, open(fichier_entree[:-4]+'.bin', 'wb') as fsort:
        contenu = fent.read()
        code = huffman.compresser(contenu)
        fsort.write(code)
        fent.close()
        fsort.close()
    return

def decompress_file(fichier_entree):
    with open(fichier_entree, 'rb') as fent, open(fichier_entree[:-4]+'_décompressé.txt', 'w', encoding='utf-8') as fsort:
        contenu = fent.read()
        chaine = huffman.decompresser(contenu)
        fsort.write(chaine)
        fent.close()
        fsort.close()
    return

def compress_image(fichier_entree):
    with open(fichier_entree, 'rb') as fent, open(fichier_entree[:-4]+'.bin', 'wb') as fsort:
        contenu = base64.b64encode(fent.read())
        code = huffman.compresser(str(contenu))
        fsort.write(code)
        fent.close()
        fsort.close()
    return

def decompress_image(fichier_entree):
    with open(fichier_entree, 'rb') as fent, open(fichier_entree[:-4]+'décompressé.bmp', 'wb') as fsort:
        contenu = fent.read()
        chaine = huffman.decompresser(contenu)
        chaine = chaine[2:-1]
        chaine = chaine.encode("ascii")
        fsort.write(base64.b64decode(chaine))
        fent.close()
        fsort.close()
    return

#compress_file("test.txt")
#decompress_file("test.bin")
compress_image("test.bmp")
decompress_image("test.bin")



