#---------EXO1---------methode01-----------------------------------------------------------------------------------

# A=(input("Valeure de A : "))
# B=(input("Valeure de B : "))
# C=(input("Valeure de C : "))
# R = A
# A = B
# B = C
# C = R
# print("Nouvelle valeure de A :", A)
# print("Nouvelle valeure de B :", B)    
# print("Nouvelle valeure de C :",C)

# ------------------methode02-----------------------------------------------------------------------------------------

# A=(input("Valeure de A : "))
# B=(input("Valeure de B : "))
# C=(input("Valeure de C : "))
# A, B, C = C, A, B
# print("Nouvelle valeure de A :", A)
# print("Nouvelle valeure de B :", B)    
# print("Nouvelle valeure de C :",C)

#---------------------------EXO2-----------------------------------------------------------------------------

# N=int(input("entrer un nombre"))
# # C = N*N*N
# C = N ** 3
# print("Le cube de cette nombre est :",C)

#---------------------------EXO3-----------------------------------------------------------------------------

# HT=float(input("entrer le prix HT"))
# NA=int(input("entrer le nombre de pieces"))
# TVH=float(input("entrer le teaux de TVH (en %)"))
# TVH = TVH / 100 
# Total_HT = HT * NA
# Montant_TVH = Total_HT * TVH
# TTC = Montant_TVH + Total_HT
# print("le prix total est :",TTC)

#------------------------------EXO4------------------------------------------------------------------------

# Nombre = float(input("entrer un nombre"))
# if Nombre > 0 :
#     print("le nombre est positif")
# elif Nombre < 0 :
#     print ("le nombre est negatif")
# else:
#     print("le nombre est null")

#---------------------------------EXO5----------------------------------------------------------------------

# X = int(input("entrer la valeur de X"))
# Y = int(input("entrer la valeur de Y"))
# if (X==0) or (Y==0) :
#     print("le produit est nul")
# elif (X>0 and Y>0) or (X<0 and Y<0) :
#     print("le produit est positif")
# else :
#     print("le produit est negatif")

#----------------------------------------EXO6--------------------------------------------------------------------

# mois = int(input("entrer un mois"))
# anne = int(input("entrer une anne"))
# if (mois < 1) or (mois > 12 ) :
#     print("errure : mois invalide")
# elif mois == 2 :
#     if anne % 4 == 0 :
#         jour = 29
#     else :
#         jour = 28
#     print("Nombre de jour est :",jour)
# elif (mois == 1)or(mois == 3)or(mois == 5)or(mois == 7)or(mois == 8)or(mois == 10)or(mois == 12) :
#     jour = 31
#     print("Nombre de jour est :",jour)
# else :
#     jour = 30
#     print("Nombre de jour est :",jour)

#---------------------------------------EXO7---------------------------------------------------------------------



