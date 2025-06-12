# Imports nécessaires pour le script
import sys
import traceback
from codecs import decode, encode

from termcolor import colored


def select_mode():
    """
    Fonction pour sélectionner le mode de codage ou de décodage.
    """
    # Demande à l'utilisateur de choisir le mode
    mode = input("Choisir le mode (codage (c) / décodage (d)) :\n").strip().lower()
    # Vérifie si l'entrée est valide
    if mode not in ["c", "codage", "d", "decodage", "décodage"]:
        print(
            colored(
                "\nVeuillez saisir un mode valide (codage (c) / décodage (d)).\n", "red"
            )
        )
        # Rappelle la fonction pour redemander le mode si l'entrée n'est pas valide
        select_mode()

    return mode


def input_value(mode):
    """
    Fonction pour obtenir la chaîne de caractères à coder ou décoder
    depuis la saisie de l'utilisateur.
    """
    input_text = "\nEntrez une chaîne de caractères à "
    input_text += "coder" if mode in ["c", "codage"] else "décoder"
    input_text += " :\n"

    # Demande à l'utilisateur d'entrer une chaîne de caractères
    value = input(input_text)

    if not value:
        # Si la chaîne est vide, affiche un message d'erreur et rappelle la fonction
        print(colored("\nVeuillez entrer une chaîne de caractères valide.", "red"))
        input_value(mode)

    return value


def decode_value(encoded_value):
    """
    Fonction pour décoder une chaîne de caractères à l'aide de l'algorithme ROT13.
    """
    return decode(encoded_value, "rot_13")


def encode_value(decoded_value):
    """
    Fonction pour encoder une chaîne de caractères à l'aide de l'algorithme ROT13.
    """
    return encode(decoded_value, "rot_13")


def main():
    """
    Fonction principale du script pour gérer le déroulement du programme
    et l'appel des fonctions de codage et décodage.
    """
    try:
        # Affiche un message d'accueil
        print(
            colored(
                "\n############## Décodage / encodage avec l'algorithme ROT13 ##############\n",
                "blue",
            )
        )
        # Demande à l'utilisateur de choisir le mode (codage ou décodage)
        mode = select_mode()

        # Demande à l'utilisateur d'entrer une chaîne de caractères
        value = input_value(mode)

        # Si le mode est codage, encode la chaîne, sinon décode la chaîne
        if mode in ["c", "codage"]:
            print(
                colored(
                    f"\nVoici votre chaîne codée avec l'algorithme ROT13 :\n{encode_value(value)}\n",
                    "green",
                )
            )
            return 0

        print(
            colored(
                f"\nVoici votre chaîne décodée avec l'algorithme ROT13 :\n{decode_value(value)}\n",
                "green",
            )
        )
        return 0

    except KeyboardInterrupt:
        # Gère l'interruption par l'utilisateur (Ctrl+C)
        print(
            colored("\nInterruption par l'utilisateur. Sortie du programme.\n", "blue")
        )
        return 1

    except Exception:
        # Gère les exceptions et affiche la trace de l'erreur
        print(traceback.format_exc())
        return 2


if __name__ == "__main__":
    # Exécute la fonction principale et quitte le programme avec le code de retour approprié
    sys.exit(main())
