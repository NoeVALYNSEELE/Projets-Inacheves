import pygame
import time
import math

pygame.init() #initialisation de pygame

#Paramètre de la fenêtre de jeu
LARGEUR, HAUTEUR = 800, 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Création d'une IA - Clicker")

#Police pour le texte
font_coder = pygame.font.Font(None, 55)
font_boutique = pygame.font.Font(None, 36)
font = pygame.font.Font(None, 36) #Police de taille 36
font2 = pygame.font.Font(None, 25) #Police secondaire

#Paramètre du bouton
bouton_coder_par = pygame.Rect(300, 175, 200, 100) # (x, y, largeur, hauteur)
bouton_acheter_autocoder = pygame.Rect(250, 540, 320, 50)
bouton_productivite = pygame.Rect(10, 540, 230, 50)

    
#Couleurs
NOIR = (0,0,0)
BLANC = (255,255,255)
VERT_NORMAL = (50, 205, 50) #bouton coder
VERT_SURVOL = (34, 139, 34) 
BLEU_NORMAL = (50, 150, 220) #boutons boutiques
BLEU_SURVOL = (0, 128, 128)

#Compteurs
nbr_lignes = 0 #Compteur de ligne de code
octets = 0 #Monnaie du jeu
Auto_coders = 0 # Nbr d'autocoders achetés
prix_autocoder = 100 #prix de l'autocoder
productivite = 1 #nbr d'octet produit par ligne
prix_productivite = 100
facteur_augmentation = 1.2 # augmentation de 20%
gain_octet_par_seconde = 0
clics_par_seconde = 0
processeur = 1 #production de chaque copilot

#Temps
dernier_tick = time.time() # Temps de la dernière génération automatique
dernier_clic = 0 # Temps du dernier clic sur "Coder"
delai_clic = 0.001 # Délai de 0.2s entre chaque clic
intervalle_autocoders = 0.5 # Fréquence de l'auto-coder (toutes les 0.5s)
dernier_clics_tick = time.time() # Temps de la dernière mise à jour du compteur de clics


#Main boucle
running = True
while running:
    
    #Fond noir
    fenetre.fill(NOIR) 

    #Position de la souris
    pos_souris = pygame.mouse.get_pos()

    #Détection du sourvol du bouton
    if bouton_coder_par.collidepoint(pos_souris):
        couleur_bouton_coder = VERT_SURVOL # Change la couleur si survol
    else:
        couleur_bouton_coder = VERT_NORMAL # Sinon couleur normale
    if bouton_acheter_autocoder.collidepoint(pos_souris):
        couleur_bouton_acheter_autocoders = BLEU_SURVOL
    else:
        couleur_bouton_acheter_autocoders = BLEU_NORMAL
    if bouton_productivite.collidepoint(pos_souris):
        couleur_bouton_productivite = BLEU_SURVOL
    else:
        couleur_bouton_productivite = BLEU_NORMAL

    #Gestion des évènements
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: #Ferme la fenetre si on appuie sur la croix
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: #Détecte clic de souris
            #print("Clic détecté !")
            temps_actuel = time.time()
            if bouton_coder_par.collidepoint(event.pos) and (temps_actuel - dernier_clic >= delai_clic):# Si clic sur le bouton
                #Bouton cliqué
                nbr_lignes = nbr_lignes+productivite #Ajoute une ligne de code
                octets = octets+productivite
                dernier_clic = temps_actuel
                dernier_clic = temps_actuel
                clics_par_seconde += 1  # Incrémente le compteur de clics
                #print(clics_par_seconde)
            if bouton_acheter_autocoder.collidepoint(event.pos) and octets >= prix_autocoder:
                Auto_coders += 1
                octets -= prix_autocoder
                prix_autocoder = int(prix_autocoder*facteur_augmentation) #augment le prix de l'autocodeur
            if bouton_productivite.collidepoint(event.pos) and octets >= prix_productivite:
                productivite +=1
                octets -= prix_productivite
                prix_productivite = int(prix_productivite*facteur_augmentation) #Augmente le prix de la productivité
        
        if event.type == pygame.KEYDOWN: #Si touche appuyé
            if event.key == pygame.K_SPACE: #Si c'est la touche espace
                print("Espace appuyé !")

    #Génération automatique de code (Copilot)
    temps_actuel = time.time()
    if temps_actuel - dernier_tick >= 1: # Toutes les secondes
        nbr_lignes += Auto_coders*processeur # Ajoute des lignes selon le nombre d'autocoders
        octets += Auto_coders*processeur # Chaque autocoder rapporte 10 octets
        dernier_tick = temps_actuel
            
    if temps_actuel - dernier_clics_tick >= 1:  # Toutes les secondes
        clics_par_seconde = 0
        dernier_clics_tick = temps_actuel
    gain_octet_par_seconde = Auto_coders + (clics_par_seconde*productivite)    
    
    
    #Affichage

    #Affichage de la boutique
    pygame.draw.rect(fenetre, (0, 128, 128), (0, 525, LARGEUR, 140))
    
    #Affichage du texte
    texte_ligne = font.render(f"Lignes de code : {nbr_lignes}", True, BLANC) #texte a afficher
    texte_octet = font.render(f"Octets : {octets}", True, BLANC)
    texte_autocoders = font.render(f"Copilot : {Auto_coders}", True, BLANC)
    texte_productivite = font.render(f"Intelligence : {productivite}", True, BLANC)
    texte_gain_par_seconde = font.render(f"Gain/Sec : {gain_octet_par_seconde}o", True, BLANC)
    fenetre.blit(texte_ligne, (10, 10))
    fenetre.blit(texte_octet, (10, 45))
    fenetre.blit(texte_autocoders, (670, 10))
    fenetre.blit(texte_productivite, (618, 45))
    fenetre.blit(texte_gain_par_seconde, (340, 10))
    
    # Affiche les coordonnées de la souris en haut à gauche
    texte_coord = font2.render(f"X: {pos_souris[0]} Y: {pos_souris[1]}", True, BLANC)
    fenetre.blit(texte_coord, (344, 40))

    #Affichage des boutons
    pygame.draw.rect(fenetre, couleur_bouton_coder, bouton_coder_par, border_radius=20) #Dessine le bouton avec bord arrondi et de la bonne couleur
    pygame.draw.rect(fenetre, couleur_bouton_acheter_autocoders, bouton_acheter_autocoder, border_radius=20)
    pygame.draw.rect(fenetre, couleur_bouton_productivite, bouton_productivite, border_radius=20)

    
    #Affiche du texte dans le bouton
    texte_coder_bouton = font_coder.render("Coder", True, NOIR) #Texte noir sur le bouton vert
    text_coder_position = texte_coder_bouton.get_rect(center=bouton_coder_par.center) #Centrer le texte dans le bouton
    texte_acheter_autocoders = font_boutique.render(f"Acheter un Copilot ({prix_autocoder}o)", True, NOIR)
    texte_acheter_autocoder_position = texte_acheter_autocoders.get_rect(center=bouton_acheter_autocoder.center)
    texte_productivite = font_boutique.render(f"Apprendre ({prix_productivite}o)", True, NOIR)
    texte_productivite_position = texte_productivite.get_rect(center=bouton_productivite.center)
    fenetre.blit(texte_coder_bouton, text_coder_position.topleft)
    fenetre.blit(texte_acheter_autocoders, texte_acheter_autocoder_position.topleft)
    fenetre.blit(texte_productivite,texte_productivite_position.topleft)

    #Rafraichit l'écran
    pygame.display.flip() 

pygame.quit() #Quitte proprement