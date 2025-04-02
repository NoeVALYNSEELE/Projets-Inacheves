def infos_input():
    print("Chiffrement/déchiffrement César : ")
    print("1. Chiffrement")
    print("2. Déchiffrement")
    mode = int(input("Choisissez le mode voulu (1 ou 2) : "))
    if mode == 1:
        print("Mode chiffrement")
        texte = input("Insérez votre texte à chiffrer ici : ")
        cle = int(input("Insérez la clé de chiffrement voulue (nombre entier) : "))
    elif mode == 2:
        print("Mode déchiffrement")
        texte = input("Insérez votre texte à déchiffrer ici : ")
        cle = int(input("Insérez la clé de chiffrement que l'on vous a fournie (nombre entier) : "))
    else:
        print("Choix invalide, veuillez retenter avec un autre chiffre !!!")
        return None, None, None
    return texte, cle, mode

def chiffrer(texte, decalage):
    texte_chiffré = ""
    for char in texte:  # Parcourir chaque caractère
        if char.isalpha():  # Vérifier si c'est une lettre
            



def main():
    texte, cle, mode = infos_input()
    if texte is not None and cle is not None and mode is not None:
        print(f"Texte: {texte}")
        print(f"Clé: {cle}")
        print(f"Mode: {mode}")
    else:
        print("Erreur dans la saisie des informations.")

if __name__ == "__main__":
    main()