import os
import random
from fonctions import *

def jouer_au_pendu():
    print('***************************************\n' \
          '*********** LE JEU DU PENDU ***********\n' \
          '***************************************\n')
    
    u_defaut = input('Souhaitez vous utiliser la banque de mots par défaut? \n' \
    'Veuillez répondre par [Y] ou par [N]:  ')

    if u_defaut == 'N' or u_defaut == 'n':
        file_name = input('Veuillez entrer le nom du fichier où se trouve votre banque de mots:  ')
        liste_mots = import_mots(file_name)
    else:
        liste_mots = import_mots()

    mot = pick_mot(liste_mots)



    return

jouer_au_pendu()