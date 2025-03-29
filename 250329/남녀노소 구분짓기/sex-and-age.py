gender = int(input().strip())
age = int(input().strip())  

if gender == 0:
    print("BOY" if age < 20 else "MAN")
else:
    print("GIRL" if age < 20 else "WOMAN")
