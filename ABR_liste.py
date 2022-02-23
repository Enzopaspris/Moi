def creation_ABR(taille):
    L = [None for i in range(taille + 1)]
    return L

def recherche(L, e, n=0):
    if len(L) > 0:
        if L[n] == e :
            return True
        elif L[2*n ] == e or L[2*n + 1] == e:
            return True
        else :
            recherche(L, e, n =+ 1)

def insertion(L, e):
    if L[0] == None :
        L[0] = e
    else :





L = creation_ABR(3)
print(L)