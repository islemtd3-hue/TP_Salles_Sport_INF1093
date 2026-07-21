# --------------------------------------------------------------------------------------
# A=int(input("entrer la valeur de A "))
# B=int(input("entrer la valeur de B "))
# C=int(input("entrer la valeur de C "))
# # R = A 
# # A = B
# # B = C
# # C = R
# A , B , C = B , C , A
# print("la nouvel valeure de A :",A,"la nouvel valeur de B :",B,"la nouvel valeur de C :",C)
# ---------------------------------------------------------------------------------------
# N=int(input("entrer un nombre"))
# C=N**3
# print("LE CUBE DE N EST :",C)
# ----------------------------------------------------------------------------------------
# PRIX=float(input("tapez le pRIX"))
# TVH=float(input("tapez le TVH"))
# NB=int(input("tapez le NB"))
# TVH=TVH / 100
# PT=PRIX*NB
# MT=PT*TVH
# TTC=MT+PT
# print("le prix total est :",TTC)
#-----------------------------------------------
# A=int(input("tapez la valeur de A") )
# if A>0:
#     print("A est positif :", A)
# elif A<0:
#     print("A est negatif:", A)
# else:
#     print("A est nul:", A) 
# -----------------------Exo5-------------------------------
X=int(input("tapez x"))
y=int(input("tapez y"))
if X > 0 and y > 0 or X<0 and y<0 :
   print("produit est positif")
elif  X <0 and y >0 :
   print("produit est negatif")   
else :
   print("X , y est null")