# très complexe à comprendre n'est pas entierement mon travail #


import pygame, sys
from pygame.locals import *
from traitement_fichier import *
from fonctions import *
pygame.init()

# initialise une fenetre appeler écran
ecran = pygame.display.set_mode((640, 480))
ecran.fill(blanc)

# permet de créer une zone cliquable nommée score_rec, elle y contiendra le texte de la variable score.
score_rec = pygame.Rect((550,5), (72,30))
zone_rec = pygame.Surface(score_rec.size)
zone_rec.fill((255,20,147))
ecran.blit(zone_rec, (550,5))

police_principale = pygame.font.SysFont(roboto ,30)
score = police_principale.render ("score", 1 , blanc)
ecran.blit(score, (560,10))

# permet de créer une zone avec du texte qui contiendra le texte de la variable debut_partie.
debut_partie = police_principale.render ("Voulez-vous commencer une nouvelle partie ?", True , (0,0,150) )
ecran.blit(debut_partie, (125,80))

# permet de créer une zone cliquable nommée oui_rec, elle y contiendra le texte de la variable oui.
oui_rec = pygame.Rect((150,200), (30,20))
zone_rec = pygame.Surface(oui_rec.size)
zone_rec.fill(blanc)
ecran.blit(zone_rec, (150,200))

oui = police_principale.render ("oui", 1 , (0,200,0) )
ecran.blit(oui, (150,200))

# permet de créer une zone cliquable nommée non_rec, elle y contiendra le texte de la variable non.
non_rec = pygame.Rect((450,200), (35,20))
zone_rec = pygame.Surface(non_rec.size)
zone_rec.fill(blanc)
ecran.blit(zone_rec, (450,200))

non = police_principale.render ("non", 1 , (200,0,0) )
ecran.blit(non, (450,200))

# permet d'initialiser différente variable :
# nbr_erreur correspond aux erreurs utilisés pour l'affichage du pendu,
# compteur est une variable que j'ai utilisé pour activer/désactiver l'affichage/utilisation de fonctionnalités
##comme des zones de texte ou encore des zones cliquable...
nbr_erreur = 0
compteur = 0

# ajout est ma variable qui contiendra les lettres du pendu,
# nom correspond aux noms d'utilisateurs,
ajout = ''
nom = ''

# cre_mot est le choix du mot en random
cre_mot = None

# permet d'initialisé la variable base_font qui est utilisé dans les zones de texte
base_font = pygame.font.Font(None, 32)

# permet d'actualisé l'affichage de la fenêtre
pygame.display.flip()

# continuer correspond à la variable utilisé pour activer/désactiver la boucle de jeu,
continuer = True
  
while continuer:
    # pygame.time.Clock.tick permet de fixer le nombre de tick
    pygame.time.Clock().tick(20)
    
    # cette boucle for permet de détecter et utiliser les interactions avec l'utilisateur
    for event in pygame.event.get():

        # ce if permet de traiter les clics de la sourri lorsqu'ils sont pressés par l'utilisateur.
        if event.type == pygame.MOUSEBUTTONDOWN:

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle score_rec et il est actif lorsque le compteur a pour valeur 0.
            if pygame.mouse.get_pressed()[0] and score_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                compteur = 0.5
                pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

                # permet de créer une zone cliquable nommée retour_debut, elle y contiendra le texte de la variable score. 
                retour_debut = pygame.Rect((10,5), (260,30))
                zone_rec = pygame.Surface(retour_debut.size)
                zone_rec.fill((255,20,147))
                ecran.blit(zone_rec, (10,5))

                score = police_principale.render ("retour à l'écran de début", 1 , blanc)
                ecran.blit(score, (20,10))
                
                # permet de créer du texte contenu dans les variables score_facile, scor_moyen et score_difficile.
                score_facile = police_principale.render ("niveau facile", 1 , (0,200,0) )
                ecran.blit(score_facile, (50,100))

                score_moyen = police_principale.render ("niveau moyen", 1 , (251,163,26) )
                ecran.blit(score_moyen, (250,100))
                
                score_difficile = police_principale.render ("niveau difficile", 1 , (200,0,0) )
                ecran.blit(score_difficile, (450,100))
                
                # cette fonction permet d'afficher le tableau des scores
                affich_score(police_principale, ecran)

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle retour_debut et il est actif lorsque le compteur a pour valeur 0.5.
            if pygame.mouse.get_pressed()[0] and compteur == 0.5 and retour_debut.collidepoint(pygame.mouse.get_pos()):
                # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

                # ce bloque permet d'afficher la première page et de rénisialisé les différentes variables
                # au fonctionnement du jeu
                reinitialise = page_debut(ecran, police_principale)
                ajout = reinitialise[0]
                nom = reinitialise[1]
                nbr_erreur = reinitialise[2]
                compteur = reinitialise[3]                
                
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle non_rec et il est actif lorsque le compteur a pour valeur 0. Si c'est le cas, le jeu s'arrete.
            if pygame.mouse.get_pressed()[0] and non_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                continuer = False
                break

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle oui_rec et il est actif lorsque le compteur a pour valeur 0.
            if pygame.mouse.get_pressed()[0] and oui_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                compteur = 1

                
                # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

                # permet de créer du texte contenu dans la variable début_partie.
                debut_partie = police_principale.render("Quelle niveau de difficulté souhaitez-vous ", True , (0,0,150) )
                ecran.blit(debut_partie, (110,50))

                # permet de créer des zones cliquable nommée facile_rec, moyen_re et difficile_rec.
                # La 1ère zone cliquable contiendra le texte de la variable facile, la secone celui de moyen et
                # la dernière celle de la variable difficile 
                facile_rec = pygame.Rect((50,100), (125,20))
                zone_rec = pygame.Surface(facile_rec.size)
                zone_rec.fill(blanc)
                ecran.blit(zone_rec, (50,100))

                facile = police_principale.render ("niveau facile", 1 , (0,200,0) )
                ecran.blit(facile, (50,100))

                moyen_rec = pygame.Rect((250,100), (135,20))
                zone_rec = pygame.Surface(moyen_rec.size)
                zone_rec.fill(blanc)
                ecran.blit(zone_rec, (250,100))

                moyen = police_principale.render ("niveau moyen", 1 , (251,163,26) )
                ecran.blit(moyen, (250,100))

                difficile_rec = pygame.Rect((450,100), (145,20))
                zone_rec = pygame.Surface(difficile_rec.size)
                zone_rec.fill(blanc)
                ecran.blit(zone_rec, (450,100))

                difficile = police_principale.render ("niveau difficile", 1 , (200,0,0) )
                ecran.blit(difficile, (450,100))

                # permet de créer et afficher le texte contenu dans les variables zone_ajout, description et description_suite.
                zone_ajout = police_principale.render ("Veuillez entrer votre nom ou pseudos ", 1 , noir )
                ecran.blit(zone_ajout, (135,180))
                
                description = pygame.font.SysFont(roboto, 25).render ('(Pour activer la saisi, veuillez choisir la difficulté, ensuite', 1 , noir )
                ecran.blit(description, (90,210))
                description_suite = pygame.font.SysFont(roboto, 25).render ('saisissez votre nom ou pseudo et appuyer sur le bouton "valider")', 1 , noir )
                ecran.blit(description_suite, (50,240))

                # permet de créer un bonton nommée valide_rec, ce dernier contiendra le texte de la variable valid.
                valid_rec = pygame.Rect((450,330), (80,30))
                valider_rec = pygame.Surface(valid_rec.size)
                valider_rec.fill((220,220,220))
                ecran.blit(valider_rec, (450,330))

                valid = police_principale.render ("Valider", 1 , noir )
                ecran.blit(valid, (455,335))

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle valid_rec et il est actif lorsque le compteur a pour valeur 1.5.
            if pygame.mouse.get_pressed()[0] and compteur == 1.5 and valid_rec.collidepoint(pygame.mouse.get_pos()):
                # si le niveau choisi est facile, alors j'ajoute "f-" devant le nom/pseudo.
                if niveau == "facile":
                    nom = "f-" + nom

                # si le niveau choisi est moyen, alors j'ajoute "m-" devant le nom/pseudo.
                elif niveau == "moyen":
                    nom = "m-" + nom
                
                # si le niveau choisi est difficile, alors j'ajoute "d-" devant le nom/pseudo.
                elif niveau == "difficile":
                    nom = "d-" + nom
                
                # j'utilise la fonction recherche_score pour savoir si un score est associer au nom/pseudo
                # s'il n'y a aucun résultat, alors il est initialisé dans le tableau grâce à nouveau_score.
                point = recherche_score(nom)
                nouveau_score(nom,point)

                compteur = 2
            
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle facile_rec et il est actif lorsque le compteur a pour valeur 1. Si c'est le cas niveau = "facile".
            if pygame.mouse.get_pressed()[0] and compteur == 1 and facile_rec.collidepoint(pygame.mouse.get_pos()):
                niveau = "facile"
                compteur = 1.5
            
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle moyen_rec et il est actif lorsque le compteur a pour valeur 1. Si c'est le cas niveau = "moyen".
            if pygame.mouse.get_pressed()[0] and compteur == 1 and moyen_rec.collidepoint(pygame.mouse.get_pos()):
                niveau = "moyen"
                compteur = 1.5
            
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle difficile_rec et il est actif lorsque le compteur a pour valeur 1. Si c'est le cas niveau = "difficile".
            if pygame.mouse.get_pressed()[0] and compteur == 1 and difficile_rec.collidepoint(pygame.mouse.get_pos()):
                niveau = "difficile"
                compteur = 1.5

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle non_rec et il est actif lorsque le compteur a pour valeur 3.
            if pygame.mouse.get_pressed()[0] and non_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 2:
                compteur = 4

                # ces variables permettent de choisir un mot de manière aléatoire grâce à la fonction choix_mot() 
                # et d'initialiser la longueur de la zone de texte nécessaire au fonctionnement du pendu.
                mot = choix_mot()
                saisie_texte = zone_texte(mot)

                # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 600, 300))

                # permet de créer et afficher le texte contenu dans la variable debut_partie, cete dernière permet d'afficher le niveau.
                debut_partie = police_principale.render(niveau, True , (0,0,150) )
                ecran.blit(debut_partie, (110,80))
            
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle oui_rec et il est actif lorsque le compteur a pour valeur 3.
            if pygame.mouse.get_pressed()[0] and oui_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 2:
                compteur = 3
                
                # permet de créer et afficher le texte contenu dans les variables zone_ajout et description.
                zone_ajout = police_principale.render("Veuillez entrer un mot dont vous voulez l'ajouter à la liste", 1 , noir )
                ecran.blit(zone_ajout, (40,250))
                
                description = pygame.font.SysFont(roboto, 25).render('(Pour valider la saisi taper sur la touche shift ou sur le bouton "valider")', 1 , noir )
                ecran.blit(description, (20,270))

                # permet de créer un bonton nommée valide_rec, ce dernier contiendra le texte de la variable valid.
                valid_rec = pygame.Rect((450,350), (80,30))
                valider_rec = pygame.Surface(valid_rec.size)
                valider_rec.fill((220,220,220))
                ecran.blit(valider_rec, (450,350))

                valid = police_principale.render ("Valider", 1 , noir )
                ecran.blit(valid, (455,355))
            
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle valid_rec et il est actif lorsque le compteur a pour valeur 4.
            if pygame.mouse.get_pressed()[0] and compteur == 3 and valid_rec.collidepoint(pygame.mouse.get_pos()):
                # la fonction ajout_mot() permet d'ajouter le mot saisie 
                cre_mot = ajout_mot(ajout)

                # si cre_mot cre_mot == "Ajout réussi", alors je génère un nouveau mot de manière alétoire et j'initialise saisie_texte
                # selon la longueur du mot, cette dernière est nécessaire au fonctionnement du pendu.
                if cre_mot == "Ajout réussi":
                    mot = choix_mot()
                    saisie_texte = zone_texte(mot)
                    compteur = 4

                    # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                    pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

                    # permet de créer et afficher le texte contenu dans la variable debut_partie, cete dernière permet d'afficher le niveau.
                    debut_partie = police_principale.render(niveau, True , (0,0,150) )
                    ecran.blit(debut_partie, (110,80))
        
        # ce if permet de détecter si une touche du clavier est enfoncé et il est actif lorsque le compteur a pour valeur 1.5,
        # avec la variable nom, j'enregistre les touches grâce à event.unicode.
        if event.type == pygame.KEYDOWN and compteur == 1.5:
            nom += event.unicode
        
        # ce if permet de détecter si une touche du clavier est enfoncé et il est actif lorsque le compteur a pour valeur 4,
        # avec la variable ajout, j'enregistre les touches grâce à event.unicode.
        if event.type == pygame.KEYDOWN and compteur == 3:
            ajout += event.unicode

            # ce if permet de détecter si une des touches shift est enfoncé, grâce à pygame.key.get_mods() & pygame.KMOD_SHIFT,
            # avec la variable nom, j'enregistre les touches grâce à event.unicode.
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                # la fonction ajout_mot() permet d'ajouter le mot saisie
                cre_mot = ajout_mot(ajout)

                # si cre_mot cre_mot == "Ajout réussi", alors je génère un nouveau mot de manière alétoire et j'initialise saisie_texte
                # selon la longueur du mot, cette dernière est nécessaire au fonctionnement du pendu.
                if cre_mot == "Ajout réussi":
                    mot = choix_mot()
                    saisie_texte = zone_texte(mot)
                    compteur = 4

                    # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                    pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

                    # permet de créer et afficher le texte contenu dans la variable debut_partie, cete dernière permet d'afficher le niveau.
                    debut_partie = police_principale.render(niveau, True , (0,0,150) )
                    ecran.blit(debut_partie, (110,80))

        # ce if permet de détecter si une touche du clavier est enfoncé et il est actif lorsque le compteur a pour valeur 5,
        # avec la variable lettre, j'enregistre les touches grâce à event.unicode.
        if event.type == pygame.KEYDOWN and compteur == 4:
            lettre = event.unicode

            # si la lettre saisi n'est pas dans mot ou si il est déjà présent dans saisie_texte, j'ajoute 1 au compteur nbr_erreur. 
            if lettre not in mot or lettre in saisie_texte:
                nbr_erreur += 1

            # si la lettre saisi est dans mot, alors je remplace les tiret par la lettre. 
            # si la lettre est plusieurs fois présente dans mot, alors elle sera ajouté autant de fois qu'elle est présente dans mot.
            if lettre in mot:
                for x in range(len(mot)):
                    if lettre == mot[x]:
                        ma_list = list(saisie_texte)
                        ma_list[x+x] = lettre
                        saisie_texte = ''.join(ma_list)

            # si niveau == "facile", alors la variable jeu prendra comme valeur la variable pendu_facile, j'y envoie le nombre d'erreur.
            if niveau == "facile":
                jeu = pendu_facile(ecran, nbr_erreur)
                
            # si niveau == "moyen", alors la variable jeu prendra comme valeur la variable pendu_moyen, j'y envoie le nombre d'erreur.
            elif niveau == "moyen":
                jeu = pendu_moyen(ecran, nbr_erreur)

            # si niveau == "difficile", alors la variable jeu prendra comme valeur la variable pendu_difficile, j'y envoie le nombre d'erreur.
            elif niveau == "difficile":
                jeu = pendu_difficile(ecran, nbr_erreur)

            # si la variable jeu a pour valeur "perdu", je rénitialise l'affiche et j'affiche perdu grâce à la variable perdu
            if jeu == "perdu":
                pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

                perdu = police_principale.render ("partie PERDU", 1 , (200,0,0) )
                ecran.blit(perdu, (250,30))

                reinitialise = page_debut(ecran, police_principale)
                ajout = reinitialise[0]
                nom = reinitialise[1]
                nbr_erreur = reinitialise[2]
                compteur = reinitialise[3]
                
                saisie_texte = zone_texte(mot)

        # si l'événement détecter est égal à QUIT, alors la boucle de jeu s'arrete. 
        # L'événement QUIT correspond à la croix rouge en haut à droite de la fenetre.
        if event.type == QUIT:
            continuer = False
        
    # si compteur == 1,5, alors j'initialise ma zone de texte grâce à la variable zone_saisie, 
    # celle-ci y integrera le texte de la variable nom à travers la variable texte.
    if compteur == 1.5:
        zone_saisie = pygame.Rect(225, 270, 200, 50)
        pygame.draw.rect(ecran, noir, zone_saisie, 2)
        texte = base_font.render(nom, True, noir)
        ecran.blit(texte, (zone_saisie.x+5, zone_saisie.y+5))
    
    #si compteur == 2, alors
    if compteur == 2:

        # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
        pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))

        # permet de créer et afficher le texte contenu dans les variables ajout_mot_liste, oui et non. 
        # Je réutilise les zones cliquables oui_rec et non_rec crée pour compteur == 0.
        ajout_mot_liste = police_principale.render("Voulez-vous ajouter un mot à la liste existante ?", True , (0,0,150) )
        ecran.blit(ajout_mot_liste, (110,80))

        oui = police_principale.render ("oui", 1 , (0,200,0) )
        ecran.blit(oui, (150,200))

        non = police_principale.render ("non", 1 , (200,0,0) )
        ecran.blit(non, (450,200))

    # si compteur == 3, alors j'initialise ma zone de texte grâce à la variable zone_saisie, 
    # celle-ci y integrera le texte de la variable ajout à travers la variable texte.
    if compteur == 3:
        zone_saisie = pygame.Rect(225, 300, 200, 50)
        pygame.draw.rect(ecran, noir, zone_saisie, 2)
        texte = base_font.render(ajout, True, noir)
        ecran.blit(texte, (zone_saisie.x+5, zone_saisie.y+5))

        if cre_mot != None:
            # si cre_mot a pour valeur doublon, alors je réinitialise l'affiche de la zone de texte et 
            # j'affiche le texte contenu dans les variables erreurs et erreurs_bis
            if cre_mot == "Doublon":
                ajout = ""
                cre_mot = None

                zone_saisie = pygame.Rect(225, 300, 200, 50)
                pygame.draw.rect(ecran, blanc, zone_saisie)

                erreur = police_principale.render ("Mot déjà présent dans la liste", 1 , (200,0,0) )
                ecran.blit(erreur, (10,360))
                
                erreur_bis = police_principale.render ("Veuillez taper un autre mot", 1 , (200,0,0) )
                ecran.blit(erreur_bis, (10,380))
    
    # si compteur == 4, alors j'initialise ma zone de texte grâce à la variable zone_saisie, 
    # celle-ci y integrera le texte de la variable ajout à travers la variable texte.
    if compteur == 4:
        zone_saisie = pygame.Rect(200, 225, 140, 32)
        pygame.draw.rect(ecran, blanc, zone_saisie)
        texte = base_font.render(saisie_texte, True, noir)
        ecran.blit(texte, (zone_saisie.x+5, zone_saisie.y+5))

        # j'initialise la variable gagne avec la fonction victoire
        gagne = victoire(saisie_texte, mot)

        # si gagne == "gagné", alors je rénitialise l'affiche et j'affiche gagné grâce à la variable perdu
        if gagne =="gagné":
            nouveau_score(nom,point+1)
            pygame.draw.rect(ecran, blanc, pygame.Rect(0,0, 700, 700))
            reinitialise = page_debut(ecran, police_principale)
            ajout = reinitialise[0]
            nom = reinitialise[1]
            nbr_erreur = reinitialise[2]
            compteur = reinitialise[3]

            succes = police_principale.render ("partie gagné", 1 , (0,200,0) )
            ecran.blit(succes, (250,30))

            saisie_texte = zone_texte(mot)

    # grâce à pygame.display.flip() j'actualise l'affichage de la fenêtre        
    pygame.display.flip()

# avec pygame.quit() j'arrete le fonctionnement de pygame
pygame.quit()

#  Pour informations:
#   compteur = 0 correspond à la page du début de jeu
#   compteur = 0.5 correspond à la page de score
#   compteur = 1 correspond à la page choix de niveau
#   compteur = 1.5 correspond à la zone de saisie de nom/pseudo, elle est active uniquement après choix de niveau
#   compteur = 2 correspond à la page où on choisi si on veut ou non ajouter un mot
#   compteur = 3 correspond à la zone de saisie d'ajout de mots, elle est active uniquement si on clique oui de la page du compteur 2
#   compteur = 4 correspond à la page de jeu du pendu
