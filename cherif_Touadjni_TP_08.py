class Chambre:
    def __init__(self, numero, etage, superficie, prix, disponible):
        self.__numero = numero
        self.__etage = etage
        self.__superficie = superficie
        self.__prix = prix
        self.__disponible = disponible

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def etage(self):
        return self.__etage

    @etage.setter
    def etage(self, etage):
        self.__etage = etage

    @property
    def superficie(self):
        return self.__superficie

    @superficie.setter
    def superficie(self, superficie):
        if superficie > 0:
            self.__superficie = superficie
        else:
            print("Superficie invalide.")

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
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, disponible):
        if disponible.lower() == "oui" or disponible.lower() == "non":
            self.__disponible = disponible.capitalize()
        else:
            print("Disponibilité invalide.")

    def afficher(self):
        print("Numéro :", self.numero)
        print("Étage :", self.etage)
        print("Superficie :", self.superficie, "m²")
        print("Prix mensuel :", self.prix, "$")
        print("Disponible :", self.disponible)

class ChambreStandard(Chambre):
    def __init__(self, numero, etage, superficie, prix, disponible, bureau):
        super().__init__(numero, etage, superficie, prix, disponible)
        self.bureau = bureau

    def afficher(self):
        super().afficher()
        print("Bureau :", self.bureau)


class ChambreLuxe(Chambre):
    def __init__(self, numero, etage, superficie, prix, disponible, balcon):
        super().__init__(numero, etage, superficie, prix, disponible)
        self.balcon = balcon

    def afficher(self):
        super().afficher()
        print("Balcon :", self.balcon)


chambres = []

chambre1 = ChambreStandard(1, "Sous-sol", 12.5, 750, "Oui", "Oui")
chambre2 = ChambreStandard(2, "Rez-de-chaussée", 13, 800, "Non", "Non")
chambre3 = ChambreLuxe(3, "Étage 2", 18, 1100, "Oui", "Oui")
chambre4 = ChambreLuxe(4, "Étage 2", 20, 1250, "Oui", "Non")

chambres.append(chambre1)
chambres.append(chambre2)
chambres.append(chambre3)
chambres.append(chambre4)

for chambre in chambres:
    chambre.afficher() 

def sauvegarder_chambres(chambres):
    fichier = open("chambres.txt", "w")

    for chambre in chambres:

        if isinstance(chambre, ChambreStandard):
            ligne = f"STANDARD;{chambre.numero};{chambre.etage};{chambre.superficie};{chambre.prix};{chambre.disponible};{chambre.bureau}\n"

        elif isinstance(chambre, ChambreLuxe):
            ligne = f"LUXE;{chambre.numero};{chambre.etage};{chambre.superficie};{chambre.prix};{chambre.disponible};{chambre.balcon}\n"

        fichier.write(ligne)

    fichier.close()


sauvegarder_chambres(chambres)

def charger_chambres():
    chambres = []

    fichier = open("chambres.txt", "r")

    for ligne in fichier:
        infos = ligne.strip().split(";")

        if infos[0] == "STANDARD":
            chambre = ChambreStandard(
                int(infos[1]),
                infos[2],
                float(infos[3]),
                float(infos[4]),
                infos[5],
                infos[6]
            )
            chambres.append(chambre)

        elif infos[0] == "LUXE":
            chambre = ChambreLuxe(
                int(infos[1]),
                infos[2],
                float(infos[3]),
                float(infos[4]),
                infos[5],
                infos[6]
            )
            chambres.append(chambre)

    fichier.close()
    return chambres

chambres_chargees = charger_chambres()

for chambre in chambres_chargees:
    chambre.afficher()

def afficher_chambres_disponibles(chambres):
    for chambre in chambres:
        if chambre.disponible == "Oui":
            chambre.afficher()


def afficher_chambres_luxe(chambres):
    for chambre in chambres:
        if isinstance(chambre, ChambreLuxe):
            chambre.afficher()

print("Chambres disponibles :")
afficher_chambres_disponibles(chambres)

print("Chambres de luxe :")
afficher_chambres_luxe(chambres)

def menu():
    chambres = []

    choix = ""

    while choix != "0":
        print("\n===== MENU =====")
        print("1. Ajouter une chambre standard")
        print("2. Ajouter une chambre de luxe")
        print("3. Afficher toutes les chambres")
        print("4. Afficher les chambres disponibles")
        print("5. Afficher les chambres de luxe")
        print("6. Sauvegarder les chambres")
        print("7. Charger les chambres")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            numero = int(input("Numéro : "))
            etage = input("Étage : ")
            superficie = float(input("Superficie : "))
            prix = float(input("Prix mensuel : "))
            disponible = input("Disponible Oui/Non : ")
            bureau = input("Bureau Oui/Non : ")

            chambre = ChambreStandard(numero, etage, superficie, prix, disponible, bureau)
            chambres.append(chambre)

        elif choix == "2":
            numero = int(input("Numéro : "))
            etage = input("Étage : ")
            superficie = float(input("Superficie : "))
            prix = float(input("Prix mensuel : "))
            disponible = input("Disponible Oui/Non : ")
            balcon = input("Balcon Oui/Non : ")

            chambre = ChambreLuxe(numero, etage, superficie, prix, disponible, balcon)
            chambres.append(chambre)

        elif choix == "3":
            for chambre in chambres:
                chambre.afficher()

        elif choix == "4":
            afficher_chambres_disponibles(chambres)

        elif choix == "5":
            afficher_chambres_luxe(chambres)

        elif choix == "6":
            sauvegarder_chambres(chambres)
            print("Les chambres ont été sauvegardées.")

        elif choix == "7":
            chambres = charger_chambres()
            print("Les chambres ont été chargées.")

        elif choix == "0":
            print("Fin du programme.")

        else:
            print("Choix invalide.")


menu()