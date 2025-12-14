#Project Euler Q1
#Sum of all multiples of 3 & 5 for first 1000 numbers

#after going online: I have been adding multiples that are the same value to the equation

value_1 = 3
value_2 = 5
max = 1000

max_1 = max//value_1
max_2 = max//value_2
common_mult = value_1*value_2

listMult_1 = []
listMult_2 = []

for loop_1 in range(1, max_1+1):
    mult_1 = value_1*loop_1
    if mult_1 >= max:
        break
    listMult_1.append(mult_1)

for loop_2 in range(1, max_2+1):
    mult_2 = value_2*loop_2
    if mult_2 >= max:
        break
    elif mult_2%common_mult == 0:
        continue
    listMult_2.append(mult_2)

final_1 = sum(listMult_1) 
final_2 = sum(listMult_2)
final = final_1+final_2

print(final)