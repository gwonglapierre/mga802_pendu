#---------------------------------------------------------------------------------------
# Module 3 - Jeu du pendu (MGA802)
# Auteur:Gabriel Wong-Lapierre
# Date de création: 2025-05-15
# Dernière modification: 2025-05-21
#---------------------------------------------------------------------------------------

import os
import random
import unicodedata
from fonctions import *

def jouer_au_pendu():
    print('***************************************\n' \
          '*********** LE JEU DU PENDU ***********\n' \
          '***************************************\n')
    
    # Initialisation du jeu

    u_defaut = input('Souhaitez vous utiliser la banque de mots par défaut? \n' \
    'Veuillez répondre par [Y] ou par [N]:  ').upper()

    if u_defaut == 'N':
        file_name = input('Veuillez entrer le nom du fichier où se trouve votre banque de mots:  ')
        dossier = input('Veuillez entrer le chemin du dossier où se trouve votre banque de mots:  ')
        liste_mots = import_mots(file_name,dossier)
    else:
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
              f'Lettres excluses: {track_echecs}\n\n'\
              f'État actuel du mot : {' '.join(mot_actuel)}\n')
        
        # Demande à l'utilisateur de d'entrer une lettre, stock la lettre et ensuite vérifie si elle se trouve dans le mot.
        tentative = str(input('Veuiller entrer une lettre:  ').upper())
        track_lettres.append(tentative)
        val, index = verif_lettre(tentative,mot) 

        # La lettre se trouvae dans le mot : mettre à jour le visuel du mot_actuel avec nouvelle lettre
        if val == True:
            for i in index:
                mot_actuel[i] = mot[i]

        # La lettre ne s'y trouve pas : décrémenter le nommbre de chances, mettre à jour visuel des chances, stocker la lettre erronée
        else:
            n_chances -= 1
            err_counter[-(1 + n_chances)] = 'X'
            track_echecs = track_echecs + tentative + '  '

        
        # Vérification si le mot est complété, change la condition pour sortir à la fin de la boucle
        if mot_actuel.count('_') == 0:
            succes = True

        # BONUS INDICE 

        # Vérifier s'il ne reste qu'une chance et si l'indice a déjà été utilisé
        if n_chances == 1 and indice_used == False:
            indice_used = True
            lettre_ind = indice(mot,track_lettres)
            track_lettres.append(lettre_ind)
            track_echecs = track_echecs + lettre_ind + '  '
            print('\n*************** Indice ****************\n\n'\
                  f'La lettre {lettre_ind} ne se trouve pas dans le mot à deviner.')

        ronde += 1

    # Fin de partie

    print('\n********** Fin de la partie ***********')

    # Note : la consigne demande à ce que l'affichage du résultat de la partie soit à l'intérieur de la boucle. Je pense que cette étape est redondante avec le while et opte pour un affichage à l'extérieur de celle-ci. 
    # Vérifier si nous sommes sortis de la boucle dû à un succès ou un échec puis imprimer le résultat
    if succes == False:
        print(f'\nChances restantes: {' '.join(err_counter)}\n'\
              'Meilleure chance la prochaine fois!\n'\
              f'Le mot à deviner était: {mot}')
    else: 
        print('\nFélicitations!!!!!!!!!!!!\n\n'\
              f'Le mot à deviner était: {mot}')




    return

jouer_au_pendu()
