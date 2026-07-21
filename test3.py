age=int(input("entrer votre age"))
if age < 18 :
    print("vous etes mineur")
elif (age >= 18 and age <= 21) :
    print("vous ete adolescent")
elif (age >= 22 and age <= 59) :
    print("vous etes adult")
else:
    print("vous etes senior")
