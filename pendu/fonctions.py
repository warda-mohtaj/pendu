import pygame

blanc = (255, 255, 255)
noir = (0, 0, 0)
vert = (0, 255, 0)

# page_debut est utilisé pour pouvoir réinitialiser l'afficha, elle englobe les différents paramètres de la première page.
def page_debut(ecran, police_principale):
    score_rec = pygame.Rect((550,5), (72,30))
    zone_rec = pygame.Surface(score_rec.size)
    zone_rec.fill((255,20,147))
    ecran.blit(zone_rec, (550,5))

    score = police_principale.render("score", 1 , blanc)
    ecran.blit(score, (560,10))

    debut_partie = police_principale.render("Voulez-vous recommencer une nouvelle partie ?", True , (0,0,150) )
    ecran.blit(debut_partie, (125,80))

    oui = police_principale.render("oui", 1 , (0,200,0) )
    ecran.blit(oui, (150,200))

    non = police_principale.render("non", 1 , (200,0,0) )
    ecran.blit(non, (450,200))
    ajout = ''
    nom = ''
    nbr_erreur = 0
    compteur = 0
    return ajout, nom, nbr_erreur, compteur

# pendu_facile correspond au pendu niveau facile, elle affiche différentes lignes, selon le nombre d'erreurs.
def pendu_facile(ecran, erreurs):
   #erreur permise 10
    if erreurs == 1:
        pygame.draw.line(ecran,(0,0,0), (250,200), (400, 200))
    if erreurs == 2:
        pygame.draw.line(ecran,(0,0,0), (300,50), (300, 200))
    if erreurs == 3:
        pygame.draw.line(ecran,(0,0,0), (300,50), (400, 50))
        pygame.draw.line(ecran,(0,0,0), (325,50), (300, 75))
    if erreurs == 4:
        pygame.draw.line(ecran,(0,0,0), (375,50), (375, 75))
    if erreurs == 5:
        pygame.draw.circle(ecran,(0,0,0), (375,90), 15, 1)
    if erreurs == 6:
        pygame.draw.line(ecran,(0,0,0), (375,105), (375, 140))
    if erreurs == 7:
        pygame.draw.line(ecran,(0,0,0), (375,105), (360, 120))
    if erreurs == 8:
        pygame.draw.line(ecran,(0,0,0), (375,105), (390, 120))
    if erreurs == 9:
        pygame.draw.line(ecran,(0,0,0), (375,140), (360, 155))
    if erreurs == 10:
        pygame.draw.line(ecran,(0,0,0), (375,140), (390, 155))
        return "perdu"

# pendu_moyen correspond au pendu niveau moyen, elle affiche différentes lignes, selon le nombre d'erreurs.
def pendu_moyen(ecran, erreurs):
    #erreur permise 6
    if erreurs == 1:
        pygame.draw.line(ecran,(0,0,0), (250,200), (400, 200))
    if erreurs == 2:
        pygame.draw.line(ecran,(0,0,0), (300,50), (300, 200))
    if erreurs == 3:
        pygame.draw.line(ecran,(0,0,0), (300,50), (400, 50))
        pygame.draw.line(ecran,(0,0,0), (325,50), (300, 75))
    if erreurs == 4:
        pygame.draw.line(ecran,(0,0,0), (375,50), (375, 75))
        pygame.draw.circle(ecran,(0,0,0), (375,90), 15, 1)
        pygame.draw.line(ecran,(0,0,0), (375,105), (375, 140))
    if erreurs == 5:
        pygame.draw.line(ecran,(0,0,0), (375,105), (360, 120))
        pygame.draw.line(ecran,(0,0,0), (375,105), (390, 120))
    if erreurs == 6:
        pygame.draw.line(ecran,(0,0,0), (375,140), (360, 155))
        pygame.draw.line(ecran,(0,0,0), (375,140), (390, 155))
        return "perdu"

# pendu_difficile correspond au pendu niveau difficile, elle affiche différentes lignes, selon le nombre d'erreurs.
def pendu_difficile(ecran, erreurs):
    #erreur permise 3
    if erreurs == 1:
        pygame.draw.line(ecran,(0,0,0), (250,200), (400, 200))
        pygame.draw.line(ecran,(0,0,0), (300,50), (300, 200))
        pygame.draw.line(ecran,(0,0,0), (300,50), (400, 50))
        pygame.draw.line(ecran,(0,0,0), (325,50), (300, 75))
    if erreurs == 2:
        pygame.draw.line(ecran,(0,0,0), (375,50), (375, 75))
        pygame.draw.circle(ecran,(0,0,0), (375,90), 15, 1)
        pygame.draw.line(ecran,(0,0,0), (375,105), (375, 140))
    if erreurs == 3:
        pygame.draw.line(ecran,(0,0,0), (375,105), (360, 120))
        pygame.draw.line(ecran,(0,0,0), (375,105), (390, 120))
        pygame.draw.line(ecran,(0,0,0), (375,140), (360, 155))
        pygame.draw.line(ecran,(0,0,0), (375,140), (390, 155))
        return "perdu"

# zone_texte est une fonction qui permet d'afficher autant de tirets qu'il y a de lettre dans mots
def zone_texte(mot):
    erreurs = 0
    while erreurs < len(mot):
        erreurs+=1
    texte = "_ " * erreurs
    return texte

# victoire permet de savoir si la saisie_texte = mot, si c'est le cas, elle return "gagné"
def victoire(saisie_texte, mot):
    reponse = ""
    for x in saisie_texte:
        if x != " ":
            reponse += x
    if reponse == mot :
        return "gagné"
   