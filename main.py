import os
import random
from fonctions import *

def jouer_au_pendu():
    print('***************************************\n' \
          '*********** LE JEU DU PENDU ***********\n' \
          '***************************************\n')
    
    # Initialisation du jeu

    # u_defaut = input('Souhaitez vous utiliser la banque de mots par défaut? \n' \
    # 'Veuillez répondre par [Y] ou par [N]:  ').upper()

    # if u_defaut == 'N':
    #     file_name = input('Veuillez entrer le nom du fichier où se trouve votre banque de mots:  ')
    #     liste_mots = import_mots(file_name)
    # else:
    #     liste_mots = import_mots()

    # Pour debug
    liste_mots = import_mots()

    # Initialisation des variables

    mot = pick_mot(liste_mots)
    n_lettres = len(mot)
    n_chances = 6
    err_counter = list('O'*n_chances)
    ronde = 1
    mot_actuel = list('_' * n_lettres)
    succes = 0

    # Début de la partie

    print('\n********* Début de la partie **********\n\n'\
        f'Le mot à deviner a {n_lettres} lettres.\n'\
        f'Vous avez droit à {n_chances} erreurs.\n'\
        'Bonne chance!\n')

    
    # Boucle de jeu

    while n_chances > 0 and succes == 0:

        # Début de la boucle et affichage l'état actuel du mot

        print(f'\n*************** Ronde {ronde} ***************\n\n\n'\
              f'Chances restantes: {' '.join(err_counter)}\n'\
                f'État actuel du mot : {' '.join(mot_actuel)}\n\n\n')
        
        # Demande à l'utilisateur de d'entrer une lettre

        tentative = input('Veuiller entrer une lettre:  ').upper()
        val, ind = verif_lettre(tentative,mot)

        if val == True:
            for i in ind:
                mot_actuel[i] = tentative
            print(' '.join(mot_actuel))
        else:
            n_chances -= 1
            err_counter[-(1+n_chances)] = 'X'

        if mot_actuel.count('_') == 0:
            succes = 1

        ronde += 1

    
    # Fin de partie

    print('\n********** Fin de la partie ***********')


    if succes == 0:
        print('\n\nT\'es nul')
    else: 
        print('\n\nFélicitations!!!!!!!!!!!!')




    return

jouer_au_pendu()

# mot = 'polyvalente'
# val, ind = verif_lettre('L',mot)
# print(val, ind)