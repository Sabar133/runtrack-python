def Arondi_crois(L):
    n = 0
    while L[n:]:
        n += 1

    a = 0
    while a < n - 1:
        indice_min = a
        b = a + 1
        while b < n:
            if L[b] < L[indice_min]:
                indice_min = b
            b += 1

        L[a], L[indice_min] = L[indice_min], L[a]
        a += 1

def Arondi_crois1(L1):
    n = 0
    while L1[n:]:
        n += 1

    a = 0
    while a < n:
        L1[a] = int(L1[a] + 0.5)
        a += 1

    Arondi_crois(L1)

    return L1

L1 = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

resultat = Arondi_crois1(L1)

print(resultat)
