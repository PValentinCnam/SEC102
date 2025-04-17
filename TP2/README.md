# Script de décodage / encodage avec l'algorithme ROT13

## Mise en place sous Windows

1. S'assurer d'avoir une installation de Python sur sa machine, sinon l'installer : https://www.python.org/downloads/

⚠️ Lors de l'installation, bien penser à sélectionner l'option "Add python.exe to PATH", sinon il faudra l'ajouter manuellement à la variable d'environnement PATH plus tard.

2. Installer la bibliothèque termcolor, pour ceci, ouvrir un teminal powershell et saisir cette commande :

⚠️ Si aucun environnement virtuel n'est activé, cette bibliothèque sera installée globalement. Si vous préférez l'installer dans un environnement virtuel, voir comment en créer un, par exemple ici : https://wikiform.fr/codespace/creer-et-utiliser-venv-sur-windows-avec-python/

```sh
pip install termcolor
```

3. Dans un terminal, se placer dans le dossier contenant le fichier `script_rot13.py`

4. Executer le script avec la commande :

```sh
py -m script_rot13
```

5. Saisir `c` pour coder une chaîne ou `d` pour décoder une chaîne, puis Entrée.

6. Saisir la valeur à coder / décoder, puis Entrée.

7. La valeur codée / décodée s'affiche.