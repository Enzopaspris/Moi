AB = [1, 2, 3, 4, 5, 6, 7]

def recherche(L, e, n=0):
    if L[n] == e :
        print("L'élément est présent")
    elif L[2*n + 1] == e or L[2*n + 2] == e:
        print("L'élément est présent")
    else :
        recherche(L, e, n =+ 1)

recherche(AB, 8)
