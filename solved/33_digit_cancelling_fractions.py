fractions_array = []
nom_product = 1
denom_product = 1

def checkIfEqual(denom, nom, a, b):
    print(nom, denom)
    are_equal = False
    if nom % 10 != 0 and denom % 10 != 0 and ((nom/denom)==(a/b)):
        are_equal = True
    return are_equal

for nominator in range(10,100):
    for denominator in range(10,100):

        denom_str = str(denominator)
        nom_str = str(nominator)
        are_equal = False

        if nom_str[0] == denom_str[0]:
            are_equal = checkIfEqual(denominator, nominator, int(nom_str[1]), int(denom_str[1]))
        elif nom_str[0] == denom_str[1]:
            are_equal = checkIfEqual(denominator, nominator, int(nom_str[1]), int(denom_str[0]))
        elif nom_str[1] == denom_str[0]:
            are_equal = checkIfEqual(denominator, nominator, int(nom_str[0]), int(denom_str[1]))
        elif nom_str[1] == denom_str[1]:
            are_equal = checkIfEqual(denominator, nominator, int(nom_str[0]), int(denom_str[0]))
        
        if are_equal and denominator > nominator:
            fractions_array.append((nominator,denominator))

for frac in fractions_array:
    nom_product *= frac[0]
    denom_product *= frac[1]

rel_factor = 1 / (nom_product/denom_product)
print(rel_factor)
