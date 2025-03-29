gender = int(input().strip())
age = int(input().strip())  

if gender == 0:
    print("MAN" if age >= 19 else "BOY")
else:
    print("WOMAN" if age >= 19 else "GIRL")
