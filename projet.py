age = int(input("Âge : "))
frequence = int(input("Fréquence cardiaque : "))
temps = float(input("Temps : "))

if frequence < 100 and temps < 6:
    print("Bonne condition")
elif frequence < 120 and temps < 8:
    print("Condition moyenne")
else:
    print("À améliorer")