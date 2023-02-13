import random
from fonctions import noir

roboto = "Roboto-Regular.ttf"

# cette fonction permet lire le fichier mots.txt.
def lecture_fichier():
    mots = ""
    f = open("mots.txt", "r", encoding="UTF-8")

    # cette boucle permet d'ajouter les lettres du fichier dans mots.
    for lettre in f:
        mots += lettre
    f.close()

    # je sépare chacun des mots grâce à split, j'utilise espace comme séparateur.
    tableau_mots = mots.split(" ")
    return tableau_mots

# cette fonction permet de choisir un mot aléatoirement dans tableau_mots grâce à random.choise.
def choix_mot():
    tableau_mots = lecture_fichier()
    mot = random.choice(tableau_mots)
    return mot

# cette fonction permet d'ajouter un mot et vérifier s'il est déjà présent dans le fichier mots.txt.
def ajout_mot(mot):
    tableau_mots = lecture_fichier()
    ma_list = ""
    tableau_mots += [mot]
    erreur = 0
    for x in tableau_mots:
        if x not in ma_list:
            ma_list += x + " "
        elif x in ma_list:
            erreur += 1
    f = open("mots.txt", "w")
    f.write(ma_list)
    if erreur > 1:
        return "Doublon"
    elif erreur <= 1:
        return "Ajout réussi"

# cette fonction permet de lire le fichier scores.txt et s'il est vide, le fichier est initialisé avec tableau_score
def lecture_tableau_score():
    tableau_score = {}

    try:
        with open("scores.txt", "r") as f:
            # cette boucle permet de séparé lignes du fichiers scores.txt en 2 variables : ancien_nom et ancien_score 
            # et de formater le dictionnaire. Le séparateur utilisé est ":".
            for mot in f.readlines():
                ancien_nom, ancien_score = mot.split(":")
                # ancien_nom = ancien_nom.strip()
                ancien_score = ancien_score.strip()
                ancien_score = int(ancien_score)
                tableau_score[ancien_nom] = ancien_score
            return tableau_score
    except:
        return tableau_score


# cette fonction permet d'écrire le nouveau_score
def nouveau_score(nom, score):
    tableau_score = lecture_tableau_score()
    
    tableau_score[nom] = score
    try:
        with open("scores.txt", "w") as f:
            # cette boucle permet d'écrire le ancien_nom et le ancien_score dans le fichiers scors.txt
            for nom, score in tableau_score.items():
                f.write(f"{nom}: {score}\n")
    except:
        print(f"Une erreur s'est produite lors de l'écriture du ancien_nom et du ancien_score dans le fichier scores.txt")


# cette fonction permet d'afficher le tableau des scores
def affich_score(police, ecran):
    tableau_score = lecture_tableau_score()
    
    with open("scores.txt", "r") as f:
        i = 130
        for ancien_nom, ancien_score in tableau_score.items():
            if ancien_nom[0:2] == "f-":
                ancien_score = (f"{ancien_nom[2::]}: {ancien_score}")
                score_difficile = police.render (ancien_score, 1 , noir )
                ecran.blit(score_difficile, (50, i))
                i += 30
        i = 130
        for ancien_nom, ancien_score in tableau_score.items():
            if ancien_nom[0:2] == "m-":
                ancien_score = (f"{ancien_nom[2::]}: {ancien_score}")
                score_difficile = police.render (ancien_score, 1 , noir )
                ecran.blit(score_difficile, (250, i))
                i += 30
        i = 130
        for ancien_nom, ancien_score in tableau_score.items():
            if ancien_nom[0:2] == "d-":
                ancien_score = (f"{ancien_nom[2::]}: {ancien_score}")
                score_difficile = police.render (ancien_score, 1 , noir )
                ecran.blit(score_difficile, (450, i))
                i += 30

# cette fonction permet de chercher s'il y a un score associé au nom entré dans le pendu
def recherche_score(nom):
    tableau_score = lecture_tableau_score()
    
    with open("scores.txt", "r") as f:
        for ancien_nom, ancien_score in tableau_score.items():
            if nom == ancien_nom:
                return ancien_score
        return 0