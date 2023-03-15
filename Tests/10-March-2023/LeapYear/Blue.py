year=int(input("enter a year"))
check=(year %4 or 400)
if check %100 == 0:
    if check != 0 :
        print("it is a leap year")
    else:
        print("it is not a leap year")
else:
    print("not possible to tell, sorry")