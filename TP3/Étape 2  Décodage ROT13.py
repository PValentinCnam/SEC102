import winreg
import codecs


# Fonction de décodage ROT13
def decode_rot13():
    try:
        with open("userassist.txt", "r", encoding='utf-8') as fichier_in, \
             open("decode_userassist.txt", "w", encoding='utf-8') as fichier_out:
            for ligne in fichier_in:
                ligne_decodee = codecs.decode(ligne.strip(), 'rot_13')
                fichier_out.write(ligne_decodee + "\n")
        print("decode_userassist.txt a été créé avec succès.")
    except Exception as e:
        print("Erreur lors du décodage ROT13 :", e)

# Exécution des fonctions
decode_rot13()