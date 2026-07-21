somme = 0
nbAchats = 0
nbGrosAchats = 0
max_montant = 0

montant = float(input("Entrer un montant (0 pour terminer): "))

while montant != 0:
    if montant < 0:
        print("Montant invalide")
    else:
        somme += montant
        nbAchats += 1

        if montant > max_montant:
            max_montant = montant

        if montant >= 100:
            nbGrosAchats += 1

    montant = float(input("Entrer un montant (0 pour terminer): "))

if nbAchats > 0:
    moyenne = somme / nbAchats
else:
    moyenne = 0

print("Nombre d'achats valides :", nbAchats)
print("Somme =", somme)
print("Moyenne =", moyenne)
print("Montant maximum =", max_montant)
print("Gros achats (>=100) =", nbGrosAchats)