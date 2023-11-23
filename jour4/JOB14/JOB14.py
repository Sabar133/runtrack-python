def my_long_word(chiffre, chaine):
    mots_long = ""
    mot = ""
    for caractere in chaine:
        if caractere != " ":
            mot += caractere
        else:
            taille_mot = 0
            for _ in mot:
                taille_mot += 1
            if taille_mot > chiffre:
                mots_long += mot + " "
            mot = ""
    taille_mot = 0
    for _ in mot:
        taille_mot += 1
    if taille_mot > chiffre:
        mots_long += mot
    return mots_long

phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, phrase)
print(resultat)