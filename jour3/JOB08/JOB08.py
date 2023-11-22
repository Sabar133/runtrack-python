def produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucune correspondance trouvée pour les produits")

# Exemples d'utilisation de la fonction
produits("fruits", "hiver")
produits("fruits", "ete")
produits("legume", "hiver")
produits("legume", "ete")
produits("inconnu", "saison")
