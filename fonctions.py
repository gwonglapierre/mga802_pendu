#---------------------------------------------------------------------------------------
# Module 3 - Jeu du pendu (MGA802)
# Auteur:Gabriel Wong-Lapierre
# Date de création: 2025-05-15
# Dernière modification: 2022-05-15
#---------------------------------------------------------------------------------------
import random
import os

# Lecture de la banque de mots
# Le fichier choisi doit absolument se trouver dans le même dossier que le script

def import_mots(file_name='mots_pendu.txt'):
    '''
    Fonction qui permet de lire un fichier .txt contenant une banque de mots et l'importe sous la forme d'une liste

    Entrée:

    file_name : Chaîne de caractère correspondant au nom du fichier où se trouve la banque de mots à importer

    Sorties:

    banque_mots : Liste contenant la banque de mots
    '''

    with open(file_name,mode='r') as banque_source:
        banque_mots = banque_source.read().split('\n')
    return banque_mots


def pick_mot(liste_mots):
        '''
    Fonction qui permet de choisir un mot au hasard parmi une liste contenant une banque de mots.

    Entrée:

    liste_mots : Liste contenant une banque de mots.

    Sorties:

    mot_choisi : Mot choisi aléatoirement dans la liste fournies.
    '''
        
        return random.choice(liste_mots)