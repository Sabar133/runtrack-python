def verification_chiffre(chiffre):
    if not isinstance(chiffre, int) or chiffre < 0:
        print("Veuillez entrer un chiffre entier et positif.")
        return

    if chiffre % 2 == 0:
        print(f"Le chiffre {chiffre} est pair.")
    else:
        print(f"Le chiffre {chiffre} est impair.")

verification_chiffre(2)
verification_chiffre(1)
verification_chiffre(4.5)
verification_chiffre(6) 
verification_chiffre(-8) 