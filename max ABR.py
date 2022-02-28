def cle_max(self):
    min = arb.racine
    while Noeud.droit != None:
        min = Noeud.droit
    return min
