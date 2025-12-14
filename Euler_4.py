
numMax = 9
mults = []

#finds all products of two values with a given max.
for i_1 in range(1,numMax+1):
    for i_2 in range(1,numMax+1):
        mult = i_1 * i_2
        #print(i_1, "x", i_2)
        mults.append(mult)

#sorting list made above.
mults.sort() #organizes values from smallest - biggest.
mults = list(set(mults)) #makes it a set which can not have dublicates, then converts back to list.
multsStr = str(mults)

#housekeeping for sublists.
mults_1 = []
mults_2 = []
mults_3 = []
i_digit = 0

#orders lists into sublists by number of digits.
for i in enumerate(mults):
    if len(str(mults[i_digit])) == 1:
        mults_1.append(mults[i_digit])
    elif len(str(mults[i_digit])) == 2:
        mults_2.append(mults[i_digit])
    elif len(str(mults[i_digit])) == 3:
        mults_3.append(mults[i_digit])
    i_digit += 1

#outputs
print("1 digit:",mults_1)
print("2 digit:",mults_2)
print("3 digit:",mults_3)