#---------------------------------------------------------------------------------------
# Module 3 - Jeu du pendu (MGA802)
# Auteur:Gabriel Wong-Lapierre
# Date de création: 2025-05-15
# Dernière modification: 2025-05-21
#---------------------------------------------------------------------------------------
import random
import os
import string

# Dictionnaire pour les accents (méthode "brute" en attendant de trouver alternative)
# temp : liste accerts langue fr À Â Ä Ç É È Ê Ë Î Ï Ô Ö Ù Û Ü Ÿ
dico_accents = {'À':'A', 'Â':'A', 'Ä':'A', 'Ç':'C', 'É':'E', 'È':'E', 'Ê':'E', 'Ë':'E',
                'Î':'I', 'Ï':'I', 'Ô':'O', 'Ö':'O', 'Ù':'U', 'Û':'U', 'Ü':'U', 'Ÿ':'Y'}


# Lecture de la banque de mots

def import_mots(file_name:str='mots_pendu.txt',dossier:str="./ressources"):
    '''
    Fonction qui permet de lire un fichier .txt contenant une banque de mots et l'importe sous la forme d'une liste

    Entrée:

    file_name : Chaîne de caractère correspondant au nom du fichier où se trouve la banque de mots à importer (str)

    dossier : Emplacement du fichier (str)

    Sorties:

    banque_mots : Liste contenant la banque de mots normalisée sans les
    '''

    with open(file_name,mode='r') as banque_source:
        banque_mots = banque_source.read().split('\n')
    return banque_mots




def lire_liste_mots(fichier="mots_pendu.txt", dossier="./ressources"):
    """Ce module permet de fournir des fonctions pour le jeu du Pendu
    Il est écrit par Marlene Sanjose dans le cadre du cours MGA802
    """
    import os

    # teste si le fichier existe
    full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

    # Transforme la chaine de caracteres en liste
    # le saut de ligne sert de separateur de champs
    word_list = words.split('\n')

    # retourne la liste de mots
    return word_list

def pick_mot(liste_mots:list):
    '''
    Fonction qui permet de choisir un mot au hasard parmi une liste contenant une banque de mots.

    Entrée:

    liste_mots : Liste contenant une banque de mots.

    Sorties:

    mot_choisi : Mot choisi aléatoirement dans la liste fournies.
    '''

    mot_choisi = random.choice(liste_mots)
        
    return mot_choisi

def verif_lettre(lettre:str,mot:str):
    '''
    Fonction qui permet de vérifier si une lettre donnée est présente dans un mot donné et, si oui, sa ou ses positions.

    Entrée:

    lettre : str d'un seul caractère représentant la lettre à tester
    mot : str représentant le mot que l'utilisateur doit deviner

    Sorties:

    val = (bool) True : la lettre se trouve au moins une fois dans le mot / False : la lettre ne se trouve pas dans le mot
    ind = (list) Indices  
    '''

    
    n_lettres = len(mot)
    ind = []
    val = False

    # Boucler chacune des lettres du mot
    for i in range(n_lettres):
        lettre_i = mot[i].upper()

        # Retirer l'accent de la lettre à vérifier (si applicable)
        if lettre_i in dico_accents.keys():
            lettre_i = dico_accents[lettre_i]

        # Comparer la lettre à valider avec la lettre indexée du mot
        if lettre == lettre_i:
            ind.append(i)
            val = True

    if val == False:
        print('\nLa lettre ne se trouve pas dans le mot!')
    else:
        print('\nLa lettre se trouve dans le mot!')
    return val, ind
    

## BONUS INDICE

def indice(mot:str, track_lettres:list):
    '''
    Fonction qui permet de donner un indice à l'utilisateur s'il lui reste une chance

    Entrée:

    mot : Le mot que l'utilisateur doit deviner
    track_lettres : Toutes les lettres qui ont été tentées par le joueur jusqu'à présent

    Sorties:

    indice : une lettre qui ne se trouve pas dans le mot et qui n'a pas été tentée encore
    '''

    # Stocker l'alphabet dans une liste puis réordonner de façon aléatoire
    alpha_list = list(string.ascii_uppercase)
    random.shuffle(alpha_list)

    # Itérer dans l'alphabet "shuffled" jusqu'à arriver à une lettre qui n'a pas été tentée et excluse du mot
    for a in alpha_list:
        if a not in track_lettres and a not in mot:
            return a



