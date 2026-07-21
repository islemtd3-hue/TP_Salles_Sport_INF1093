class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.numero = numero
        self.nom = nom
        self.succursale = succursale
        self.duree = duree
        self.prix = prix
        self.actif = actif

    def afficher(self):
        print(self.numero, self.nom, self.succursale)