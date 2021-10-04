from datetime import date
AJD=date.today()
An_actuel = AJD.year
Mois_actuel=AJD.month
Jour_actuel=AJD.day
J_naissance=int(input("Quelle est ton jour de naissance ?"))
M_naissance=int(input("Quelle est ton mois de naissance ?"))
A_naissance=int(input("Quelle est ton année de naissance ?"))

if (M_naissance>Mois_actuel) or (M_naissance==Mois_actuel and J_naissance>Jour_actuel):
    Age= An_actuel-A_naissance-1
else :
    Age = An_actuel-A_naissance
print("Tu as",Age,"ans.")
