inventaire = []


def chercher_objet(nom_objet):
    for element in inventaire:
        if element["nom"].lower() == nom_objet.lower():
            return element
    return None


def ajouter_ou_mettre_a_jour():
    nom = input("Entrez le nom de l'objet : ").strip()

    if nom == "":
        print("Le nom ne peut pas être vide.")
        return

    try:
        quantite = int(input("Entrez la quantité : "))
        if quantite <= 0:
            print("La quantité doit être supérieure à 0.")
            return
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return

    objet_trouve = chercher_objet(nom)

    if objet_trouve is not None:
        objet_trouve["quantite"] += quantite
        print(f"Quantité mise à jour : {objet_trouve['nom']} (x{objet_trouve['quantite']})")
    else:
        nouvel_objet = {
            "nom": nom,
            "quantite": quantite
        }
        inventaire.append(nouvel_objet)
        print(f"Objet ajouté : {nom} (x{quantite})")


def afficher_inventaire():
    if len(inventaire) == 0:
        print("L'inventaire est vide.")
        return

    print("\n--- Inventaire magique ---")
    for index, objet in enumerate(inventaire, start=1):
        print(f"{index}. {objet['nom']} (x{objet['quantite']})")


def supprimer_objet():
    nom = input("Entrez le nom de l'objet à supprimer : ").strip()

    if nom == "":
        print("Le nom ne peut pas être vide.")
        return

    objet_trouve = chercher_objet(nom)

    if objet_trouve is not None:
        inventaire.remove(objet_trouve)
        print(f"L'objet '{objet_trouve['nom']}' a été supprimé.")
    else:
        print("Objet introuvable dans l'inventaire.")


def afficher_menu():
    print("\n====== MENU ======")
    print("1. Ajouter / Mettre à jour un objet")
    print("2. Afficher l'inventaire")
    print("3. Supprimer un objet")
    print("4. Quitter")


while True:
    afficher_menu()
    choix = input("Choisissez une option : ").strip()

    if choix == "1":
        ajouter_ou_mettre_a_jour()
    elif choix == "2":
        afficher_inventaire()
    elif choix == "3":
        supprimer_objet()
    elif choix == "4":
        print("Au revoir, aventurier !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")