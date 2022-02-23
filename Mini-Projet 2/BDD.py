import sqlite3
import sys

data_art = [(1, "ALPHA WANN"), (2, "NEKFEU"), (3, "DAMSO"), (4, "ORELSAN")
,(5,"7JAWS"), (6,"PNL"), (7,"SCH"), (8,"LUV RESVAL")]

data_al = [(1, 1, "DON DADA MIXTAPE", 2020), (2, 1, "UNE MAIN LAVE L'AUTRE", 2018)
, (3, 3, "QALF", 2020), (4, 2,"LES ETOILES VAGABONDES", 2019),
(5, 8, "ETOILE NOIRE", 2021),(6, 4, "CIVILISATION", 2021),
(7, 5, "JE VOIS LES COULEURS", 2021), (8, 7, "JVLIVS II", 2021),
(9, 6, "DEUX FRERES", 2019), (10, 2, "FEU", 2015)]

co = sqlite3.connect("test.db")
print("Connexion à la base réussie")
curs = co.cursor()

curs.execute("DROP TABLE IF EXISTS artiste")
curs.execute('''CREATE TABLE IF NOT EXISTS artiste(
    idArtiste INTEGER PRIMARY KEY,
    nom TEXT NOT NULL
    )''')

curs.execute("DROP TABLE IF EXISTS album")
curs.execute('''CREATE TABLE IF NOT EXISTS album(
    idAlbum INTEGER PRIMARY KEY,
    idArtiste INTEGER NOT NULL,
    nom_Al TEXT NOT NULL,
    annee INTEGER NOT NULL
    )''')

curs.executemany("INSERT INTO artiste(idArtiste, nom) VALUES (?, ?)", data_art)
curs.executemany("INSERT INTO album(idAlbum, idArtiste, nom_Al, annee) VALUES (?, ?, ?, ?)",data_al)
co.commit()

def menu():
    demande = input("Que voulez vous faire ? (Ecrivez le nombre correspondant)"
    "\n1. Ajouter un élément d'une table"
    "\n2. Enlever un élément d'une table"
    "\n3. Entrer une commande SQL"
    "\n4. Voir la base"
    "\n5. Informations sur la base"
    "\n6. Quitter")
    if demande == '1':
        print(50 * "-")
        ajouter_element()
    elif demande == '2':
        print(50 * "-")
        supp_element()
    elif demande == '3':
        print(50 * "-")
        com_SQL()
    elif demande == '4':
        print(50 * "-")
        afficher()
    elif demande == '5':
        print(50 * "-")
        infos()
    elif demande == '6' :
        print(50 * "-")
        leave()
    else :
        return print(f"{demande} n'est pas une entrée valide, veuillez réessayer")

def ajouter_element():
    add = input("Dans quelle table voulez vous ajouter un élément ? (Artiste / Album) ")
    add = add.lower() # met en minuscule
    if add == "artiste":
        nv_artiste = input("Quelle est le nom de l'artiste que vous voulez ajouter ?")
        nv_artiste = nv_artiste.upper() # met en majuscule
        nv_id = len(data_art) + 1
        curs.execute("INSERT INTO artiste(idArtiste, nom) VALUES (?, ?)",(nv_id, nv_artiste))
        co.commit()
        print(f"La commande a bien été éxécuté")
    elif add == "album":
        nv_album = input("Quelle est le nom de l'album que vous voulez ajouter ?")
        nv_album = nv_album.upper() # met en majuscule
        id_art = input("Quelle est l'id de l'artiste qui l'a fait ?")
        nv_annee = input("En quelle année est-il sortie ?")
        nv_id = len(data_al) + 1
        curs.execute("INSERT INTO album(idAlbum, idArtiste, nom_Al, annee) VALUES (?, ?, ?, ?)",(nv_id, id_art, nv_album, nv_annee))
        co.commit()
        print(f"La commande a bien été éxécuté")
    else :
        print(f"{add} n'est pas une table existante, veuillez réessayer")
        ajouter_element()

def supp_element():
    delete = input("Dans quelle table voulez vous suprimmer un élément ? (Artiste / Album) ")
    delete = delete.lower() # met en minuscule
    if delete == "artiste":
        name = input("Quelle est le nom de l'élément ?")
        name = name.upper() # met en majuscule
        id = input("Quelle est son identifiant de l'élément ?")
        curs.execute("DELETE FROM artiste WHERE idArtiste = ? AND nom = ?",(id, name))
        co.commit()
        print(f"L'élément {name} a bien été suprimmé")
    elif delete == "album":
        name = input("Quelle est le nom de l'élément ?")
        name = name.upper() # met en majuscule
        id = input("Quelle est son identifiant de l'élément ?")
        curs.execute("DELETE FROM album WHERE idAlbum = ? AND nom_Al = ?",(id, name))
        co.commit()
        print(f"L'élément {name} a bien été suprimmé")
    else :
        print(f"{delete} n'est pas une table existante, veuillez réessayer")
        supp_element()
    print(50 * "-")

def com_SQL():
    commande = input("Entrer votre commande SQL :")
    curs.execute(commande)
    print(curs.fetchall())
    print(f"La commande a bien été éxécuté")
    dm = input("Voulez vous revenir au menu ? Oui/Non")
    dm = dm.lower() # met en minuscule
    if dm == "non":
        com_SQL()
    else :
        return


def afficher():
    nom_tab = input("Quelle table voulez vous afficher ? (Artiste / Album)")
    nom_tab = nom_tab.lower() # met en minuscule
    if nom_tab == "artiste":
        print("Nombre total de lignes : ", len(data_art))
        print(50 * "-")
        curs.execute("SELECT * FROM artiste ")
        print(curs.fetchall())
        dm = input("Voulez vous revenir au menu ? Oui/Non")
        dm = dm.lower()
        if dm == "non":
            afficher()
        else :
            return
    elif nom_tab == "album" :
        print("Nombre total de lignes : ", len(data_al))
        print(50 * "-")
        curs.execute("SELECT * FROM album ")
        print(curs.fetchall())
        dm = input("Voulez vous revenir au menu ? Oui/Non")
        dm = dm.lower() # met en minuscule
        if dm == "non":
            afficher()
        else :
            return
    else :
        print(f"{nom_tab} n'est pas une entrée valide, veuillez réessayer")
        afficher()
    print(50 * "-")

def infos():
    add = input("Dans quelle table voulez vous des informations ? (Artiste / Album) ")
    add = add.lower() # met en minuscule
    if add == "artiste":
        print(f"La Table artiste contient",len(data_art),"éléments et 2 attributs :"
        "\n     idArtiste: nombre entier, ne doit pas être vide (clé PRIMAIRE)"
        "\n     nom : texte, ne doit pas être vide")
        dm = input("Voulez vous revenir au menu ? Oui/Non")
        dm = dm.lower() # met en minuscule
        if dm == "non":
            infos()
        else :
            return
    elif add == "album":
        print(f"La Table artiste contient",len(data_al),"éléments et 4 attributs :"
        "\n     idAlbum: nombre entier, ne doit pas être vide, (clé PRIMAIRE)"
        "\n     idArtiste: nombre entier, ne doit pas être vide,"
        "\n     nom_Al: texte, ne doit pas être vide"
        "\n     annee: nombre entier, ne doit pas être vide")
        dm = input("Voulez vous revenir au menu ? Oui/Non")
        dm = dm.lower() # met en minuscule
        if dm == "non":
            infos()
        else :
            return
    else :
        print(f"{add} n'est pas une table existante, veuillez réessayer")
        infos()

def leave():
    curs.close()
    print("Déconnexion à la base réussie")
    sys.exit()  #Arrêt du programme

while True:
    menu()