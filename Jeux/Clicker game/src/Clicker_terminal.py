import time

def afficher_lignes(lignes):
    """Affiche le nombre actuel de lignes de code."""
    print(f"Lignes de code écrites : {lignes}")

def ajouter_ligne(lignes):
    """Ajoute une ligne de code et affiche le compteur mis à jour."""
    lignes += 1
    afficher_lignes(lignes)
    return lignes

def main():
    """Boucle principale du jeu."""
    lignes_de_code = 0  # Initialisation du compteur
    
    while True:
        input("Appuie sur Entrée pour coder une ligne...")  # Attend une entrée
        lignes_de_code = ajouter_ligne(lignes_de_code)  # Mise à jour du compteur
        time.sleep(0.2)

# Lancer le jeu
main()