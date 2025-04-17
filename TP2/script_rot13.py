import sys
import traceback
from codecs import decode, encode

from termcolor import colored


def select_mode():
    mode = input("Choisir le mode (codage (c) / décodage (d)) :\n").strip().lower()

    if mode not in ["c", "codage", "d", "decodage", "décodage"]:
        print(
            colored(
                "\nVeuillez saisir un mode valide (codage (c) / décodage (d)).\n", "red"
            )
        )
        select_mode()

    return mode


def input_value(mode):
    input_text = "\nEntrez une chaîne de caractères à "
    input_text += "coder" if mode in ["c", "codage"] else "décoder"
    input_text += " :\n"

    value = input(input_text)

    if not value:
        print(colored("\nVeuillez entrer une chaîne de caractères valide.", "red"))
        input_value(mode)

    return value


def decode_value(encoded_value):
    return decode(encoded_value, "rot_13")


def encode_value(decoded_value):
    return encode(decoded_value, "rot_13")


def main():
    try:
        print(
            colored(
                "\n############## Décodage / encodage avec l'algorithme ROT13 ##############\n",
                "blue",
            )
        )
        mode = select_mode()
        value = input_value(mode)
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
        print(
            colored("\nInterruption par l'utilisateur. Sortie du programme.\n", "blue")
        )
        return 1

    except Exception:
        print(traceback.format_exc())
        return 2


if __name__ == "__main__":
    sys.exit(main())
