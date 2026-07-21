with open("etudiants.txt", "r") as fichier:
    lignes = fichier.readlines()

for i, nom in enumerate(lignes, start=1):
    print(f"{i}. {nom.strip()}")

print(f"Nombre total de lignes : {len(lignes)}")
