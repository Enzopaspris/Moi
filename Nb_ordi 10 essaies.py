from random import randint

nb_ordi=randint(1,100)
print("nb_ordi :",nb_ordi)
nb_essais=1
nb_utilisateur=-1
print("Tu as 10 essais pour trouver le nombre entre 1 et 100")

while nb_ordi!=nb_utilisateur and nb_essais<11:
    nb_utilisateur=int(input("Quel est le nombre ?"))
    print("essai :",nb_essais)
    if(nb_utilisateur<nb_ordi):
        print("C'est plus")
    elif(nb_utilisateur>nb_ordi):
        print("C'est moins")
    nb_essais=nb_essais+1

if nb_ordi==nb_utilisateur:
    print("Bravo tu as touvé en",nb_essais-1,"essais")
else:
    print("Dommage le nombre était le",nb_ordi)