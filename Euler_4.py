#Project Euler Q4
#finds the largest porduct of two 3 digit numbers that is a pallendrome.

numMin = 1
numMax = 9
prods = []
mults = []

#finds all products of two values with a given max.
for i_1 in range(numMin,numMax+1):
    for i_2 in range(numMin,numMax+1):
        prod = i_1 * i_2
        #print(i_1, "x", i_2)
        prods.append(prod)
        mults.append([i_1,i_2])
        #mults.append(i_2)

#sorting the list of prods made above.
##prods.sort() #organizes values from smallest - biggest.
##prods = list(set(prods)) #makes it a set which can not have dublicates, then converts back to list.

#housekeeping for sublists.
prods_1 = []
prods_2 = []
prods_3 = []
prods_4 = []
prods_5 = []
prods_6 = []

i_digit = 0

#orders lists into sublists by number of digits.



#tests to get rid of lists for each number of digits
#goes straight into dividing
for i in enumerate(prods):
    if len(str(prods[i_digit])) == 2:
        spl_1 = str(prods[i_digit])
        spl_1.split(chr)
    elif len(str(prods[i_digit])) == 3:
        prods_3.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 4:
        prods_4.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 5:
        prods_5.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 6:
        prods_6.append(int(prods[i_digit]))
    i_digit += 1

#outputs
print(prods)
print(mults)
print(mults[12], "=", prods[12])
print(spl_1)

#for testProd_2 in prods_2:
    #print(testProd_2)

#Create code that finds the index of the mults that make a given prod. (i.e. index of prod *2, +1?)

#print("1 digit:",prods_1)
#print("2 digit:",prods_2)
#print("3 digit:",prods_3)