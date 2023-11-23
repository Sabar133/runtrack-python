def liste_entier(liste, index):
    if 0 < index < len(liste) - 1:
        somme_voisins = liste[index - 1] + liste[index + 1]
        liste[index] = liste

L = [1, 2, 3, 4, 5]

print(L)

second_index = L[1]
print(second_index)

liste_entier(L, 3)
L2 = [6, 7, 8, 9, 10]
print(L2)

dernier_index = L[-1]
print(dernier_index)