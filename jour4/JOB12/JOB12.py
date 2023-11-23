def Ordre(liste):
    i = 0
    taille = 0
    for element in liste:
        taille += 1

    while i < taille:
        indice_minimum = i
        j = i + 1
        while j < taille:
            if liste[j] < liste[indice_minimum]:
                indice_minimum = j
            j += 1

        liste[i], liste[indice_minimum] = liste[indice_minimum], liste[i]
        i += 1

L = [64, 25, 12, 22, 11]

print("Liste avant le tri :", L)

Ordre(L)

print("Liste après le tri :", L)