import winreg
import codecs

# Fonction de lecture de la base de registre
def lire_userassist():
    chemin_base = r"Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist"
    clé_hcu = winreg.HKEY_CURRENT_USER

    # Création automatique du fichier userassist.txt
    with open("userassist.txt", "w", encoding='utf-8') as f:
        try:
            with winreg.OpenKey(clé_hcu, chemin_base) as cle:
                nb_sous_cles, _, _ = winreg.QueryInfoKey(cle)
                for i in range(nb_sous_cles):
                    sous_cle_nom = winreg.EnumKey(cle, i)
                    with winreg.OpenKey(cle, sous_cle_nom + r"\Count") as sous_cle:
                        nb_valeurs = winreg.QueryInfoKey(sous_cle)[1]
                        for j in range(nb_valeurs):
                            nom_valeur, _, _ = winreg.EnumValue(sous_cle, j)
                            f.write(nom_valeur + "\n")
            print("userassist.txt a été créé avec succès.")
        except Exception as e:
            print("Erreur lors de la lecture de la base de registre :", e)


# Exécution des fonctions
lire_userassist()
