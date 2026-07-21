n = 1
while n != 0:
    try:
        n = int(input("Entrez un nombre: "))
        if n == 0:
            raise ValueError(" FIN DU PROGRAMME !!! ")
        print("La table de multiplication jusqua 10 est: ")
        for i in range(11):
            print(f" {n} * {i} = {n*i}" )
    except ValueError as e:
        print( e)
    except Exception as e:
        print(" Vous avez une erreur: ", e)
    