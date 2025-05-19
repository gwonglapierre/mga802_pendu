import os
import random
import unicodedata
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

    # Pour debug                                            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% À RETIRER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liste_mots = lire_liste_mots()


    # Choix du mot 

    mot = pick_mot(liste_mots).upper()
    
    # Initialisation des variables

    n_lettres = len(mot)
    n_chances = 6
    err_counter = list('O' * n_chances)
    ronde = 1
    mot_actuel = list('_' * n_lettres)
    succes = False
    indice_used = False
    track_lettres = []
    track_echecs = ''

    # Début de la partie

    print('\n********* Début de la partie **********\n\n'\
        f'Le mot à deviner a {n_lettres} lettres.\n'\
        f'Vous avez droit à {n_chances} erreurs.\n'\
        'Bonne chance!\n')

    
    # Boucle de jeu

    while n_chances > 0 and succes == False:

        # Début de la boucle et affichage de l'état actuel du mot

        print(f'\n*************** Ronde {ronde} ***************\n\n'\
              f'Chances restantes: {' '.join(err_counter)}\n'\
              f'Lettres échouées: {track_echecs}\n\n'\
              f'État actuel du mot : {' '.join(mot_actuel)}\n')
        
        # Demande à l'utilisateur de d'entrer une lettre

        tentative = str(input('Veuiller entrer une lettre:  ').upper())
        track_lettres.append(tentative)
        val, ind = verif_lettre(tentative,mot)

        if val == True:
            for i in ind:
                mot_actuel[i] = mot[i]
            #print(' '.join(mot_actuel))
        else:
            n_chances -= 1
            err_counter[-(1+n_chances)] = 'X'
            track_echecs = track_echecs+tentative+'  '

        


        if mot_actuel.count('_') == 0:
            succes = True

        # BONUS INDICE 

        if n_chances == 1 and indice_used == False:
            indice_used = True

            continue

        ronde += 1

    # Fin de partie

    print('\n********** Fin de la partie ***********')

    # Note : la consigne demande à ce que l'affichage du résultat de la partie soit à l'intérieur de la boucle. Je pense que cette étape est redondante avec le while et opte pour un affichage à l'extérieur de celle-ci. 
    if succes == False:
        print(f'\nChances restantes: {' '.join(err_counter)}\n'\
              'Meilleure chance la prochaine fois!\n'\
              f'Le mot à deviner était: {mot}')
    else: 
        print('\nFélicitations!!!!!!!!!!!!\n\n'\
              f'Le mot à deviner était: {mot}')




    return

jouer_au_pendu()
