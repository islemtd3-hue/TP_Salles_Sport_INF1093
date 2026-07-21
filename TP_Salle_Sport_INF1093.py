class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = 1
        self.__prix = 1
        self.__actif = "Non"

        self.duree = duree
        self.prix = prix
        self.actif = actif

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, succursale):
        self.__succursale = succursale

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, duree):
        if duree > 0:
            self.__duree = duree
        else:
            print("Durée invalide.")

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if prix > 0:
            self.__prix = prix
        else:
            print("Prix invalide.")

    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, actif):
        if actif.lower() == "oui":
            self.__actif = "Oui"
        elif actif.lower() == "non":
            self.__actif = "Non"
        else:
            print("État invalide.")

    def afficher(self):
        print(self.numero, self.nom, self.succursale,
              self.duree, self.prix, self.actif)


class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier


class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach


m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui")
m2 = MembrePremium(2, "Marc Bouchard", "Est", 6, 80, "Oui", "Oui")

m1.afficher()
m2.afficher()
class MembreStandard(Membre):
    def _init_(self, numero, nom, succursale, duree, prix, actif, casier):
        super()._init_(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

    def afficher(self):
        print("STANDARD")
        print(self.numero, self.nom, self.succursale,
              self.duree, self.prix, self.actif, self.casier)


class MembrePremium(Membre):
    def _init_(self, numero, nom, succursale, duree, prix, actif, coach):
        super()._init_(numero, nom, succursale, duree, prix, actif)
        self.coach = coach

    def afficher(self):
        print("PREMIUM")
        print(self.numero, self.nom, self.succursale,
              self.duree, self.prix, self.actif, self.coach)


m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui")
m2 = MembreStandard(2, "Marc Bouchard", "Est", 6, 40, "Non", "Non")
m3 = MembrePremium(3, "Sophie Nguyen", "Centre-ville", 12, 80, "Oui", "Oui")
m4 = MembrePremium(4, "Karim Haddad", "Ouest", 24, 75, "Oui", "Non")

membres = [m1, m2, m3, m4]

for membre in membres:
    membre.afficher()
    membres = []

m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui")
m2 = MembreStandard(2, "Marc Bouchard", "Est", 6, 40, "Non", "Non")
m3 = MembrePremium(3, "Sophie Nguyen", "Centre-ville", 12, 80, "Oui", "Oui")
m4 = MembrePremium(4, "Karim Haddad", "Ouest", 24, 75, "Oui", "Non")

membres.append(m1)
membres.append(m2)
membres.append(m3)
membres.append(m4)

for membre in membres:
    membre.afficher()