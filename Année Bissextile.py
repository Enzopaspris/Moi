annee=int(input("Donne moi une année supérieur a 1582, je te dirais si oui ou non elle est bissextile"))
if annee>=1582:
    if (annee%4==0 and not annee%100==0) or annee%400==0:
        print(annee,"est une année bissextile")
    else :
        print(annee,"n'est pas une année bissextile ")
else:
    print("L'année que tu as choisis est inférieur a 1582")