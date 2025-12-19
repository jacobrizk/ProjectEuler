for i in enumerate(prods):
    if len(str(prods[i_digit])) == 1:
        prods_1.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 2:
        prods_2.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 3:
        prods_3.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 4:
        prods_4.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 5:
        prods_5.append(int(prods[i_digit]))
    elif len(str(prods[i_digit])) == 6:
        prods_6.append(int(prods[i_digit]))
    i_digit += 1
