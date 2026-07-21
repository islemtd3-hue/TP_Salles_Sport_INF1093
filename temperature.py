temperatures = []

with open("temperature.txt", "r") as fichier:
    for ligne in fichier:
        temperatures.append(float(ligne.strip()))

if len(temperatures) == 0:
    print("Le fichier est vide")
else:
    print(f"Min : {min(temperatures)}")
    print(f"Max : {max(temperatures)}")
    print(f"Moyenne : {sum(temperatures) / len(temperatures):.1f}")
