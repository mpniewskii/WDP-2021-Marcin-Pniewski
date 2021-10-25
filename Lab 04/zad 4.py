print("Podaj boki prostokata")
boki = input()
boki = boki.split(" ")
print(boki)
if int(boki[0]) and int(boki[1]) >0:
    pole = int(boki[0]) * int(boki[1])
    print(pole)
    obwod = 2*int(boki[0]) + 2*int(boki[1])
    print(obwod)
else:
    print("niepoprawne dane")