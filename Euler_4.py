#Project Euler Q4
#finds the largest porduct of two 3 digit numbers that is a pallendrome.

numMin = 100
numMax = 999
prods = []
mults = []

#finds all products of two values with a given max.
for i_1 in range(numMin,numMax+1):
    for i_2 in range(numMin,numMax+1):
        prod = i_1 * i_2
        prods.append(prod)
        mults.append([i_1,i_2])

#housekeeping for pallendrome list.
prodsPal = []

indexProd = 0

for i_prods in prods:
    testProd = str(i_prods)
    revProd = testProd[::-1]
    if testProd == revProd:
        prodsPal.append(i_prods)
    indexProd += 1

#outputs
print(max(prodsPal))