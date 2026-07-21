def tous_uniques(liste):
    elements = set()

    for x in liste:
        if x in elements:
            return False

        elements.add(x)

    return True


print(tous_uniques([1, 2, 3, 4]))
print(tous_uniques([1, 2, 3, 1]))
