def Valeur(liste):

 maximum = max(liste)
 minimum = min(liste)
 
 return maximum, minimum

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = Valeur(L)

maximum, minimum = resultat
print("la valeur max est", maximum)
print("la valeur min est :", minimum)