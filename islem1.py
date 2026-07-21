# nombre=int(input("entrer un nombre"))

# if (nombre % 2 == 0):
#     print("le nombre est paire")
# else :
#     print("le nombre est impaire")

# if (nombre > 0):
#     print("le nombre est positif")
# else :
#     print("le nombre est negatif")

# n1=float(input("entrer le premier nombre"))
# n2=float(input("entrer le deuxieme nombre"))
# n3=float(input("entrer le troisieme nombre"))
# max = n1
# if (n2 > max) :
#     max = n2
# if (n3 > max):
#     max = n3
#     print("le grand nombre est :",max)

# nombre=int(input("entrer un nombre"))
# for i in range(nombre+1,nombre+11) :
#     print (i)

#  nombre=int(input("entrer un nombre: "))
# for i in range(1, 101) :
#     print(nombre, "X", i , "=", nombre * i)

try:
    nombre=int(input("entrer un nombre: "))
    while nombre !=0:
        i=1
    while i <= 10 :
            print(nombre, "X", i , "=", nombre * i)
            i += 1
    nombre=int(input("entrer un nombre: "))
    print("programme terminer")    
except ValueError:
    print(" entrer un nombre")



