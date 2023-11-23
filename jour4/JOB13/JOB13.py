def pas_de_doublons(liste):
    sans_doublons = []

    for a in liste:
        if a not in sans_doublons:
            sans_doublons +=[a]

    return sans_doublons

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

resultat = pas_de_doublons(L)


print(resultat)