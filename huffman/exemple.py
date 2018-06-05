from modules.bitstring import bitstring
from modules import bson

Voitures = {"citroen":3,"renaud":5}
chaine = bson.dumps(Voitures) #on transforme le dictionnaire en binary string
print(chaine)
chaine = bitstring.BitArray(chaine) #on initialise l'objet bitstring
print(chaine)
chaine = chaine.bin #puis on le transforme en chaine de caractère de 0 et de 1
print(chaine)

