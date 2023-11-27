def my_sort(liste):
    
    n = len(liste) 
    coups = 0     

    tri_effectue = False
    while not tri_effectue:
        tri_effectue = True  

        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]

                tri_effectue = False

                coups += 1

    print("Nombre total de coups nécessaires pour trier la liste :", coups)

    return liste

ma_liste = [5, 2, 9, 1, 5, 6]
liste_trie = my_sort(ma_liste)

print("Liste triée :", liste_trie)