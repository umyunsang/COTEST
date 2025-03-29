gender = int(input())
age = int(input())

if gender == 0:
    if age < 20: print("BOY")
    else: print('MAN')

else:
    if age < 20: print("GIRL")
    else: print('WOMAN')